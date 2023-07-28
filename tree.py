class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_odd_levels(root):
    if not root:
        return

    print_odd_levels_helper(root, 1)

def print_odd_levels_helper(node, level):
    if not node:
        return

    if level % 2 == 1:
        print(node.val)

    print_odd_levels_helper(node.left, level + 1)
    print_odd_levels_helper(node.right, level + 1)
    
#Example:
# create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_odd_levels(root)  
