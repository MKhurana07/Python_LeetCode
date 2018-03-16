from BST import Node
from BST import Binary_Tree

def build_from_PreIn(preorder, inorder):
    if  inorder and preorder:
        index = inorder.index(preorder[0])
        root = Node(inorder[index])
        root.left = build_from_PreIn(preorder[1:index+1], inorder[:index])
        root.right = build_from_PreIn(preorder[index+1:], inorder[index+1:])
        return root

def build_from_PostIn(postorder, inorder):
    if  inorder and postorder:
        index = inorder.index(postorder.pop())
        root = Node(inorder[index])
        root.right = build_from_PostIn(postorder, inorder[index+1:])
        root.left = build_from_PostIn(postorder, inorder[:index])
        return root

tree = Binary_Tree()
tree.root = build_from_PreIn([3,9,20,15,7],[9,3,15,20,7])
tree.print()
tree2 = Binary_Tree()
tree2.root = build_from_PostIn([9,15,7,20,3],[9,3,15,20,7])
tree2.print()
