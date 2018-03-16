from BST import Node

def validate_tree(root):
    if not root or (not root.left and not root.right):
        return True
    #for an imbalanced tree, there has to be cond to check if one of the childs is none
    if (root.left and root.right and root.left.value < root.value and root.right.value > root.value) or (root.left.value < root.value and not root.right) or (root.right.value > root.value and not root.left):
        return validate_tree(root.left) and validate_tree(root.right)
    return False

n = Node(2)
n.left = Node(1)
n.left.left = Node(0)
n.right = Node(3)
print(validate_tree(n))
