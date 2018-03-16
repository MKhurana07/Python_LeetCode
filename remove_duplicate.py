def removeduplicate(l):
    length = len(l)
    i = 0
    while i < length:
        if i>0 and l[i-1] == l[i]:
            del(l[i])
            length = length - 1
        i = i+1
    return len(l)
print(removeduplicate([1,2,3,3,4,4,5]))
