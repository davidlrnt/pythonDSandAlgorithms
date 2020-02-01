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

#EX-2: RETURN A LIST OF NODE VALUES FROM A TREE IN Breadth-first traversal ORDER:
# 	['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I']

def BFS(root):
	nodequeue = [root]
	seen = []

	while nodequeue:
		curr = nodequeue.pop()
		seen.append(curr.val)
		if curr.left:
			nodequeue.insert(0,curr.left)
		if curr.right:
			nodequeue.insert(0,curr.right)

	return seen


print(BFS(a))



