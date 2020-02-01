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


def DFS(root):
	print(root.val)
	if root.left is None and root.right is None:
		return
	if root.left:
		DFS(root.left)
	if root.right:
		DFS(root.right)


DFS(a)





