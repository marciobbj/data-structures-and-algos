from trees import Tree, TreeNode

"""
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.

Space Complexity: O(V) since, an extra visited array is needed of size V.
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

time = 0


def dfs(entry_point):
    global time
    node = tree.nodes.get(entry_point)
    node.color = "yellow"
    tree.traversal_tree.append(node)
    for child in node.neighbours:
        if child.color == "black":
            child.visited = True
            child.parent = node
            child.level = node.level + 1
            dfs(child.title)
    node.color = "green"
    time += 1


dfs("A")

print(tree)
print(time)