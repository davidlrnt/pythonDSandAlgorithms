class Tree: 
    def __init__(self, node): 
        self.root_node = node


    def find_min(self):
        curr = self.root_node
        while curr.left:
            curr = curr.left
        return curr.val


    def find_max(self):
        curr = self.root_node
        while curr.right:
            curr = curr.right
        return curr.val

    def insert(self, node):
        curr = self.root_node
        if curr.val > node.val:
            while curr.val > node.val:
                curr = curr.left
        elif curr.val < node.val: 
            print(curr.val)       
            while curr.val < node.val:
                curr = curr.right

        print(curr.val)
        if curr.val > node.val:
            print("L")
            curr.left = node
        else:
            print("R")
            curr.right = node

        return node