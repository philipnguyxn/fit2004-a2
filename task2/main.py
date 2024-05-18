from collections import deque
from typing import List, Optional, Annotated


def allocate(
        preferences: List[List[int]],
        officers_per_org: List[List[int]],
        min_shifts: int,
        max_shifts: int,
) -> Optional[Annotated[List[List[List[int]]], "allocation"]]:
    if min_shifts > max_shifts:
        return None

    graph = Graph(preferences, officers_per_org, min_shifts, max_shifts)
    graph.edmonds_karp()

    for edge in graph.adjacency_list[graph.sink]:
        if edge.residual_edge.flow != edge.residual_edge.capacity:
            return None

    return []


class Edge:
    def __init__(self, from_node: int, to_node: int, capacity: int, residual_edge=None):
        self.from_node = from_node
        self.to_node = to_node
        self.flow = 0
        self.capacity = capacity
        self.residual_edge: Optional[Edge] = residual_edge


class Graph:
    DAYS_IN_A_MONTH = 30
    SHIFTS_IN_A_DAY = 3

    def __init__(
            self,
            preferences: List[List[int]],
            officers_per_org: List[List[int]],
            min_shifts: int,
            max_shifts: int,
    ):
        self.no_officers = len(preferences)
        self.no_companies = len(officers_per_org)

        # Define the indices of source, officer's supernode, and sink in the graph
        self.source = self.no_officers * 2 + self.SHIFTS_IN_A_DAY + self.no_companies
        # self.officers_supernode = self.source + 1
        self.sink = self.source + 1

        # Initialize adjacency list
        self.adjacency_list: List[List[Edge]] = [[] for _ in range(self.sink + 1)]

        # Define shift indices in the graph
        shift_indices = [self.no_officers * 2 + shift for shift in range(self.SHIFTS_IN_A_DAY)]

        # Add edge between the source and officer supernode with the capacity is
        # the total of minimum shifts for all officers
        # self._add_edge(self.source, self.officers_supernode, self.no_officers * min_shifts)

        for i, officer in enumerate(preferences):
            # Add edge between the officer supernode and each officer with the capacity is
            # the maximum number of shifts each officer can work per month
            # self._add_edge(self.officers_supernode, i, max_shifts - min_shifts)
            self._add_edge(self.source, i, min_shifts)
            self._add_edge(i, i + 2, min_shifts)
            self._add_edge(self.source, i + 2, max_shifts - min_shifts)

            for shift in range(self.SHIFTS_IN_A_DAY):
                choice = officer[shift]

                if choice:
                    shift_index = shift_indices[shift]

                    # Add edges between officers and shifts with the capacity is the number of days in a month
                    # if the officer prefer the shift
                    self._add_edge(i + 2, shift_index, self.DAYS_IN_A_MONTH)

        companies_indices = [shift_indices[-1] + 1 + i for i in
                             range(self.no_companies)]

        for i, company in enumerate(officers_per_org):
            company_index = companies_indices[i]

            # Add edge between each pair of day and company and sink with the capacity is
            # the total number of officers requested by that company for the whole day
            self._add_edge(company_index, self.sink, sum(company) * self.DAYS_IN_A_MONTH)

            for j, no_officers in enumerate(company):
                shift_index = shift_indices[j]

                # Add edge between each shift and pair of day and company with the capacity is the number
                # of officers requested by each company per shift
                self._add_edge(shift_index, company_index, no_officers * self.DAYS_IN_A_MONTH)

    def _add_edge(self, from_node: int, to_node: int, capacity: int):
        augmented_edge = Edge(from_node, to_node, capacity)
        residual_edge = Edge(to_node, from_node, capacity, augmented_edge)
        augmented_edge.residual_edge = residual_edge

        self.adjacency_list[from_node].append(augmented_edge)
        self.adjacency_list[to_node].append(residual_edge)

    def _bfs(self, from_node: int, to_node: int, parent: List[Edge]):
        # Initial setup
        queue = deque([from_node])
        visited = [False] * (self.sink + 1)

        queue.append(from_node)
        visited[from_node] = True

        # Serve the front until the queue is empty
        while queue:
            current = queue.popleft()

            # Visit all adjacent vertices if they are not visited
            for edge in self.adjacency_list[current]:
                residual = edge.capacity - edge.flow

                if not visited[edge.to_node] and residual > 0:
                    queue.append(edge.to_node)
                    visited[edge.to_node] = True
                    parent[edge.to_node] = edge

                    if edge.to_node == to_node:
                        return True

        return False

    def edmonds_karp(self) -> int:
        # Initial setup
        parent: List[Optional[Edge]] = [None] * (self.sink + 1)
        max_flow = 0

        # Increase flows if there are augmented paths
        while self._bfs(self.source, self.sink, parent):
            path_flow = float("inf")
            to_node = self.sink

            # Find the bottleneck along the augmented path
            while to_node != self.source:
                edge = parent[to_node]
                path_flow = min(path_flow, edge.capacity - edge.flow)
                to_node = edge.from_node

            to_node = self.sink

            # Decrease the augmented and residual flows along
            # the augmented path
            while to_node != self.source:
                edge = parent[to_node]

                # Increase the augmented flow
                edge.flow += path_flow

                # Decrease the residual flow
                edge.residual_edge.flow -= path_flow

                to_node = edge.from_node

            max_flow += path_flow

        return max_flow
