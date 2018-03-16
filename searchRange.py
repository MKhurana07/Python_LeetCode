def searchRange(nums, val):
    i = 0
    start=[-1,-1]
    while nums[i]<val and i < len(nums)-1 :
        i = i +1
    if nums[i] == val:
        start[0] = i
        while nums[i] == val:
            i = i +1
        start[1] = i -1 
    return start

print(searchRange([1,2,3,3,4,4,4,5],0))
