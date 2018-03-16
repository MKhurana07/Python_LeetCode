def sliding_maximal(num, slide):
    maximals = []
    for outer in range(len(num)-slide+1):
        max = findmax(num[outer:outer+slide])
        maximals.append(max)

    return maximals
def findmax(num):
    num.sort()
    return num[-1]
print(sliding_maximal([1,2,3,4,5,6],3))
