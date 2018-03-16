def mergeSortedArray(a,m,b,n): #merge b into a, so no new space
    while n>0:
        if a[m-1] >= b[n-1]:
            a[m+n-1] = a[m-1]
            m = m-1
        elif m <=0 or a[m-1] < b[n-1]:
            a[m+n-1] = b[n-1]
            n = n-1
    return a

print(mergeSortedArray([1,2,3,0,0,0,],3,[2,3,4],3))
            
