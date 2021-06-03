class TreeNode:
    def __init__(self, title, neighbours=[], color="black"):
        self.neighbours = neighbours
        self.title = title
        self.color = color
        self._visited = False
        self.parent = None
        self.level = 0

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        self._visited = value

    def __repr__(self) -> str:
        return self.title


class Tree:
    def __init__(self, nodes):
        self.nodes = nodes
        self.traversal_tree = []

    def __repr__(self) -> str:
        if self.traversal_tree:
            return " -> ".join([e.title for e in self.traversal_tree])
        return self.traversal_tree