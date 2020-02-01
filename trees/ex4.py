from Node import Node;
from BinaryTree import Tree;

a = Node(20)
b = Node(10)
c = Node(30)
d = Node(5)
e = Node(15)
f = Node(25)
g = Node(35)
h = Node(1)
i = Node(28)

#			20
#		   /   \
#		  10   30
#		 / \   / \
#		5  15 25 35
#	   /      \
#	  1        28

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
f.right = i

#EX-2: RETURN A LIST OF NODE VALUES FROM A TREE IN Breadth-first traversal ORDER:
# 	

tree = Tree(a)

e = tree.find_min()
c = tree.find_max()

d = tree.insert(Node(7))
f = tree.insert(Node(8))


# print(e)
# print(c)
print(d)
print(f)