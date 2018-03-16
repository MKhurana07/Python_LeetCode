def sqrt(a):
    l,r = 0, a
    while l <=r:
        mid = (r+1)//2
        if mid*mid <= a < (mid+1)*(mid+1):
            return mid
        elif mid*mid > a:
            r = mid -1
        else:
            l = mid +1

print(sqrt(8))
