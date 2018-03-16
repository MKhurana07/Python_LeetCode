import random

def combo(n,k):
    resultset= set()
    
    for i in range(n):
        for m in range(n-i):
            lis = []
            j=0
            while j<k:
                lis.append(i+m)
                j=j+1
            resultset.add(tuple(lis))
    return resultset


def combine( n, k):
    ans = []
    stack = []
    x = 1
    while True:
        l = len(stack)
        if l == k:
            ans.append(stack[:])
        if l == k or x > n:
            if not stack:
                return ans
            x = stack.pop() + 1
        else:
            stack.append(x)
            x += 1


print(combo(4,2))
print(combine(4,2))

