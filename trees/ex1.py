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

#EX-1: Return list of lists with all the possible paths from root to leaf (add just the node values to the list):
# 	[['A', 'B', 'D', 'H'], ['A', 'B', 'E'], ['A', 'C', 'F', 'I'], ['A', 'C', 'G']]

def DFS(root, path = [], results = []):
	path.append(root.val)
	if root.left is None and root.right is None:
		results.append( path )
		return results
	if root.left:
		DFS(root.left, path.copy(), results)
	if root.right:
		DFS(root.right, path.copy(), results) 
	
	return results


print(DFS(a))



