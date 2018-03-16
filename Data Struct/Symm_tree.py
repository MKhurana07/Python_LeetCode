from Binary_Tree import BinaryTree

def symmetric_tree(root):
    def symm(root1, root2):
        if not root1 and not root2 or not root1.left and not root2.left or not root1.right and not root2.left :
            return True
        if (not root1.left and root2.right) or (not root2.right and root1.left) or (not root1.right and root2.left) or (root1.right and not root2.left):
            return False
        if root1.left and root1.right and root2.left and root2.right:
            if root1.left.value == root2.right.value and root1.right.value == root2.left.value:
                return symm(root1.left, root1.right) and symm(root2.left, root2.right)
            else:
                return False
        return False
    return symm(root.left, root.right)

myTree = BinaryTree(1)
myTree.insertLeftChild(2)
myTree.insertRightChild(2)
#myTree.insert(2)
#myTree.insert(3)

print(symmetric_tree(myTree))
