from Node import Node;

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")

#			A
#		   / \
#		  B   C
#		 / \ / \
#		D  E F G
#	   /      \
#	  H        I

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
f.right = i

#EX-2: RETURN A LIST OF NODE VALUES FROM A TREE IN POSTORDER:
# 	['H', 'D', 'B', 'E', 'I','F', 'G', 'C', 'A']

def DFS(root, visited = []):
	if root.left is None and root.right is None:
		visited.append(root.val)
	else:
		if root.left:
			DFS(root.left, visited)
		if root.right:
			DFS(root.right, visited)
		visited.append(root.val)
	return visited


print(DFS(a))



