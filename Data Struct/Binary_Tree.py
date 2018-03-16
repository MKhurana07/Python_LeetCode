class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    def insertRightChild(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.right = self.right
            self.right = tree
    def insertLeftChild(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.left = self.left
            self.left = tree
    def preorder(self,root):
        if root != None:
            print(root.rootid)
            root.preorder(root.getLeftChild())
            root.preorder(root.getRightChild())
    def inorder(self,root):
        if root != None:
            root.inorder(root.getLeftChild())
            print(root.rootid)
            root.inorder(root.getRightChild())
    def postorder(self,root):
        if root:
            root.postorder(root.getLeftChild())
            root.postorder(root.getRightChild())
            print(root.rootid)
    
myTree = BinaryTree("Maud")
myTree.insertLeftChild("Bob")
myTree.insertRightChild("Tony")
myTree.insertRightChild("Steven")
myTree.preorder(myTree)
myTree.inorder(myTree)
myTree.postorder(myTree)
            

