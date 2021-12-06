"""
Using the preorder traversal method, we first visit the root, the visit all the nodes from 
the left side, then visit all nodes on the right side

1. Visit the root node
2. Calling preorder (left-subtree)
3. Calling preorder (right subtree)
 """

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def preorder(self, root):
        if root is not None:
            left = self.preorder(root.left)
            right = self.preorder(root.right)
            return [root.val] + left + right
        else:
            return []

root = Node(50)
root.right = Node(53)
root.left = Node(20)

root.left.left = Node(11)
root.left.right = Node(22)

root.right.left = Node(52)
root.right.right = Node(78)

print(root.preorder(root))