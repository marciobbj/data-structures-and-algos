from trees.trees import Tree, TreeNode

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