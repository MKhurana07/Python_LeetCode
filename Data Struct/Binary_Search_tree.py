class Node():
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
    def insert(self,val):
        if val.rootid < self.rootid:
             if self.getLeftChild() != None:
                self.left.insert(val)
             else:
                self.left = Node(val)
                
        elif val.rootid > self.rootid:
            if self.getRightChild() != None:
                self.right.insert(val)
            else:
                self.right = Node(val)
        
    def find(self,val):
        if self:
            if self.rootid == val:
                print(self.rootid)
                return 1
        if self.right:
            if val > self.rootid:
                self.right.find(val)
        if self.left:
            if val < self.rootid:
                self.left.find(val)
        else:
            return 0
    def preorder(self):
        if self != None:
            print(self.rootid)
        if self.getLeftChild():
            self.getLeftChild().preorder()
        if self.getRightChild():
            self.getRightChild().preorder()
    def inorder(self):
        if self.getLeftChild():
            self.getLeftChild().inorder()
        if self:
            print(self.rootid)
        if self.getRightChild():
            self.getRightChild().inorder()
    def postorder(self):
        if self.getLeftChild():
            self.getLeftChild().postorder()
        if self.getRightChild():
            self.getRightChild().postorder()
        if self:
            print(self.rootid)
    def size(self, node):
        if not node:
            return 0

        else:
            res =  self.size(self.getLeftChild()) + 1 + self.size(self.getRightChild())
            return res

class BinarySearchTree():

    def __init__(self):
        self.root = None

    def addroot(self,val):
        self.root = val
        
    def insert(self,val):
        if self.root == None:
            self.addroot(val)
        else:
            self.root.insert(val)
            
    def find(self,val):
        if self.root == val:
            return 1
        else:
            return self.root.find(val)

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
    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()
    def postorder(self):
        self.root.postorder()
    def size(self):
        if not self.root:
            return
        self.root.size(self.root)
node = Node(10)
myTree = BinarySearchTree()
myTree.insert(node)
node = Node(4)
node2 = Node(11)
myTree.insert(node)
myTree.insert(node2)

##myTree.insertLeftChild("Bob")
##myTree.insertRightChild("Tony")
##myTree.insertRightChild("Steven")
myTree.preorder()
print("------------")
myTree.inorder()
print("----------------")
myTree.postorder()
print(myTree.find(4))
print(myTree.root.rootid)
print(myTree.size())

            

