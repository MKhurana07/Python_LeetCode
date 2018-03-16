class Node():
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self,val):
        if val == self.value:
            return 
        elif val> self.value:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)
        elif val < self.value:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
    def print_in_order(self):
        if self == None:
            return
        if self.left: 
            self.left.print_in_order()
        print(self.value)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        if self == None:
            return
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.left.print_pre_order()
        print(self.value)

    def print_post_order(self):
        if self == None:
            return
        print(self.value)
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()

    def find(self, val):
        if self.value == val:
            return "found"
        if val< self.value:
            if self.left:
                return self.left.find(val)
            else:
                return "not found"
        if val > self.value:
            if self.right:
                return self.right.find(val)
            else:
                return "not found"
    def size(self):
        if not self:
            return 0
        res = 0
        if self.left:
            res = res + self.left.size()
        if self.right:
            res = res + self.right.size()
        res = res + 1
        return res

    def height(self):
        if not self:
            return 0
        if self.left and self.right:
            return 1 + max(self.left.height(),self.right.height())
        elif not self.left and self.right:
            return 1 + self.right.height()
        elif not self.right and self.left:
            return 1 + self.left.height()
        else:
            return 1
    def min(self):
        if not self:
             return "not found"
        if self.left:
            return self.left.min()
        else:
            return self.value

    def max(self):
        if not self:
            return "not found"
        if self.right:
            return self.right.max()
        else:
            return self.value

    def maxdepth(self):
        if not self:
            return "no depth"
        left_dep = right_dep = 0
        if self.left:
            left_dep = self.left.maxdepth()
        if self.right:
            right_dep = self.right.maxdepth()
        if left_dep > right_dep:
            return left_dep + 1
        else:
            return right_dep + 1

    def isBST(self):
        if not self:
            return 0
        flag = 0
        if self.left and self.right:
            if self.left.value < self.value and self.right.value > self.value:
                return self.left.isBST() and self.right.isBST()
            else:
                return 0
        elif not self.right and self.left:
            if self.left.value < self.value:
                return self.left.isBST()
            else:
                return 0
        elif not self.left and self.right:
            if self.right.value > self.value:
                return self.right.isBST()
            else:
                return 0
        return 1
    def compare(self,node):
        if not self or not node:
            return 0
        if self.value == node.value:
            if self.left and node.left:
                return self.left.compare(node.left)
            elif self.left and not node.left or node.left and not self.left:
                return 0
            else:
                return 1
            if self.right and node.right:
                return self.right.compare(node.right)
            elif not self.right and node.right or self.right and not node.right:
                return 0
            else:
                return 1
        else:
            return 0

    def delete_nodes(self):
            if self == None:
                return
            if not self.left and not self.right:
                del self
            elif self.left:
                self.left.delete_nodes()
            elif self.right:
                self.right.delete_nodes()

    def diameter(self):
            if not self:
                return 0
            l_ht=r_ht=l_diam=r_diam=0
            if self.left:
                l_ht = self.left.height()
                l_diam = self.left.diameter()
            if self.right:
                r_ht = self.right.height()
                r_diam = self.right.diameter()
            return max((l_ht + r_ht + 1),max(l_diam,r_diam))
                    

class Binary_Tree():
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.root.insert(val)
     
    def print(self):
        if self.root == None:
            print("The tree is empty")
        else:
            self.root.print_in_order()

    def find(self, val):
        if not self.root:
            return "not found"
        return self.root.find(val)

    def size(self):
        if not self.root:
            return "empty tree"
        else:
           return self.root.size()

    def min(self):
        if not self.root:
            return "empty tree"
        return self.root.min()
    def max(self):
        if not self.root:
            return "empty tree"
        return self.root.max()

    def maxdepth(self):
        if not self.root:
            return "empty tree"
        return self.root.maxdepth()
    def isBST(self):
        if not self.root:
            return 0
        if 1 == self.root.isBST():
            return "yes"
        else:
            return "no"
    def compare(self,tree):
        if not tree.root or not self.root:
            return 0
        return self.root.compare(tree.root)
    def delete_nodes(self):
        if not self.root:
            return
        self.root.delete_nodes()
    def diameter(self):
        if not self.root:
            return 0
        return self.root.diameter()
        
        
        
        
        
    
myTree = Binary_Tree()
myTree.insert(5)
myTree.insert(4)
myTree.insert(40)
myTree.insert(32)
myTree.print()
print(myTree.find(4))
print(myTree.size())
print(myTree.root.height())
print(myTree.min())
print(myTree.max())
print(myTree.maxdepth())
print(myTree.isBST())
another_Tree = Binary_Tree()
another_Tree.insert(5)
another_Tree.insert(4)
another_Tree.insert(40)
another_Tree.insert(32)
print(myTree.compare(another_Tree))
print(another_Tree.diameter())
print("del")
myTree.delete_nodes()
myTree.print()
