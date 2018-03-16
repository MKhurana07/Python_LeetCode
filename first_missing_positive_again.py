def first_missing_positive(num):
    num.sort()
    for i in range(0,len( num)):
        if num[i] <=0:
            continue
        if num [ i] != num[i-1]+1:
            return num[i-1]+1
        return -1

print(first_missing_positive([0,-1,2,3]))
