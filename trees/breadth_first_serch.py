class TreeNode:
    def __init__(self, title, neighbours=[]):
        self.neighbours = neighbours
        self.title = title
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


A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")

A.neighbours = [B, C]
B.neighbours = [C]
C.neighbours = [D, F]
D.neighbours = [E]
E.neighbours = [F]
F.neighbours = [D]

tree = Tree({"A": A, "B": B, "C": C, "D": D, "E": E, "F": F})

from queue import Queue

queue = Queue()


def bfs(entry_point):
    first_node = tree.nodes.get(entry_point)
    first_node.visited = True
    queue.put(first_node)
    while not queue.empty():
        node = queue.get()
        tree.traversal_tree.append(node)
        for child in node.neighbours:
            if not child.visited:
                child.visited = True
                child.parent = node
                child.level = node.level + 1
                queue.put(child)


bfs("C")

print(tree)