def removeElement(l,x):
    length = len(l)
    i = 0
    while i < length:
        if l[i] == x:
            del(l[i])
            length = length -1
        else:
            i = i +1
    return length
print(removeElement([1,2,3,2,2,3,2, 3,4,2],2))
