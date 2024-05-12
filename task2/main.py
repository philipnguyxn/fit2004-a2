from typing import List, Optional, Annotated


def allocate(preferences: List[List[int]], officers_per_org: List[List[int]]) -> Optional[
    Annotated[List[List[List[int]]], 'allocation']]:
    return None


class Graph:
    def __init__(self, preferences: List[List[int]], officers_per_org: List[List[int]]):
        self.adj_matrix: List[List[int]] = []

    def _add_edge(self):
        return None

    def _bfs(self, s: int, t: int, parent: List[int]):
        # Initial setup
        queue = []
        visited = []

        queue.append(s)
        visited[s] = True

        # Serve the front until the queue is empty
        while queue:
            u = queue.pop(0)

            # Visit all adjacent vertices if they are not visited
            for v, flow in enumerate(self.adj_matrix[u]):
                if not visited[v] and flow > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    def _edmonds_karp(self, source: int, sink: int):
        # Initial setup
        parent = [-1]
        max_flow = 0

        # Increase flows if there are augmented paths
        while self._bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink

            # Find the bottleneck along the augmented path
            while s != source:
                path_flow = min(path_flow, self.adj_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            # Decrease the augmented and residual flows along the augmented path
            while v != source:
                u = parent[v]

                # Decrease the augmented flow
                self.adj_matrix[u][v] -= path_flow

                # Increase the residual flow
                self.adj_matrix[u][v] += path_flow

                v = parent[v]

            # For debugging
            path = []
            v = sink

            while v != source:
                path.append(v)
                v = parent[v]

            path.append(source)
            path.reverse()
            print(path, path_flow)
