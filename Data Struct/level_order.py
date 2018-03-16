from BST import Binary_Tree

def level_order(r):
    stack = []
    stack.append(r.root)
    answer =[[r.root.value]]
    count = 1
    while stack:
        temp = stack.pop(0)
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
        count = count -1
        if count ==0:
            answer = answer + [[ item.value for item in stack]]
            count = len(stack)
    return answer

myTree = Binary_Tree()
myTree.insert(5)
myTree.insert(4)
myTree.insert(40)
myTree.insert(32)
print(level_order(myTree))

def low_level_order(r): #bottom up
    def show(r, height):
        res =[]
        if height ==1:
            res.append(r.value)
        elif height>1:
            show(r.left, i-1)
            show(r.right, i-1)
        return res

    height = r.height()
    res1 =[[]]
    for i in range(height):
        res1 = res1 + [show(r, i)]
    return res1

    

myTree = Binary_Tree()
myTree.insert(5)
myTree.insert(4)
myTree.insert(40)
myTree.insert(32)
print(low_level_order(myTree.root))
