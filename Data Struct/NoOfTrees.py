from BST import Node,Binary_Tree

def number_of_BST(n):
    tree = {}
    tree[0]=1
    tree[1]=1
    for i in range(2,n+1):
        tree[i]=0
        for j in range(i):
            tree[i] = tree[i] + tree[j]*tree[i-j-1]
    return tree[n]

print(number_of_BST(4))

def PrintT(n):
    def print_Trees(first, last):
        trees =[]
        for i in range(first, last +1):
            for j in print_Trees(first,i-1):
                for y in print_Trees(i+1,last):
                   # print("hi")
                    BT = Binary_Tree()
                    root = Node(i)
                    root.left = j
                    root.right = y
                    BT.root = root
                    trees.append(root)
        return trees or [None]
    return print_Trees(1,n)


print(PrintT(4))
