from trees.trees import Tree, TreeNode
from queue import Queue

"""
Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
"""

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


bfs("A")

print(tree)