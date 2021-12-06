"""
Using the postorder traversal method, we first visit all the nodes from 
the left and right side and then visit the root

1. Calling postorder (left-subtree)
2. Calling postorder (right subtree)
3. Visit the root node
 """

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def postorder(self, root):
        if root is not None:
            left = self.postorder(root.left)
            right = self.postorder(root.right)
            return left + right + [root.val] 
        else:
            return []

root = Node(50)
root.right = Node(53)
root.left = Node(20)

root.left.left = Node(11)
root.left.right = Node(22)

root.right.left = Node(52)
root.right.right = Node(78)

print(root.postorder(root))