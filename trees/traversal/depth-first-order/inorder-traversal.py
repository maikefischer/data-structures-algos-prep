"""
Using the inorder traversal method, we first visit the left subtree 
of the original tree. Then we will traverse the root node of the tree
and lastly the right subtree of the original tree.

1. Calling Inorder (left-subtree)
2. Visit the root node
3. Calling Inorder (right subtree)
 """

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def inorder(self, root):
        if root is not None:
            left_list = self.inorder(root.left)
            right_list = self.inorder(root.right)
            return left_list + [root.val] + right_list
        else:
            return []


root = Node(50)
root.right = Node(53)
root.left = Node(20)

root.left.left = Node(11)
root.left.right = Node(22)

root.right.left = Node(52)
root.right.right = Node(78)

print(root.inorder(root))