NO_CHARS = 4


def _char_to_index(char: str) -> int:
    return ord(char) - ord('A')


class SuffixTrieNode:
    def __init__(self):
        self.children = [None] * NO_CHARS
        self.indexes = []


class SuffixTrie:
    def __init__(self, text: str):
        self.root = SuffixTrieNode()
        self.text = text

    

class SuffixTreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.children = [None] * NO_CHARS


class SuffixTree:
    def __init__(self, text: str):
        self.text = text
        self.root = SuffixTreeNode(-1, -1)  # Sentinel values for the root node


class OrfFinder:
    def __init__(self, genome: str):
        self.genome = genome
        self.suffix_tree = SuffixTree(genome)

    def _insert_key(self, root: TrieNode, key: str):
        curr_node = root

        # Insert each character of key into the trie if it doesn't exist
        for char in key:
            if curr_node.children[ord(char) - ord('A')] == None:
                new_node = TrieNode()

                curr_node.children[ord(char) - ord('A')] = new_node

            # Move the pointer to the next trie node
            curr_node = curr_node.children[ord(char) - ord('A')]

        # Increment word_count to implies that there's a new node has been added
        curr_node.word_count += 1

    def _search_key(self):
        pass
