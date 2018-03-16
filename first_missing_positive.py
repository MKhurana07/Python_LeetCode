def first_missing_positive(nums):
    nums.sort()
    for i in range(0,len(nums)-1):
        if nums[i+1] != nums[i]+1 and nums[i]+1>0:
            return (nums[i]+1)
    return -100

print(first_missing_positive([2,-1,4,1,3]))

