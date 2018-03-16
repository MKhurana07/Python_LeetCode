def duplicates_twice(num):
    k =len(num)
    i=2
    while i <k:
        if num[i] == num[i-1] and num[i-1]==num[i-2]:
            del num[i]
            k=k-1
        i = i+1
    return k

print(duplicates_twice([1,1,1,2,2,3,3]))
