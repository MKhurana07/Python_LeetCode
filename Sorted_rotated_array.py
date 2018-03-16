def search_rotated_array(nums,val):
    i = 0
    if val > nums[i]:
        while nums[i+1]> nums[i] and i <len(nums):
            if val == nums[i]:
                return i
            i = i+1
    elif val < nums[i]:
        while nums[i+1]>nums[i] and i < len(nums):
            i = i +1
        while i < len(nums):
            if val == nums[i]:
                return i
            i = i +1
    elif val == nums[i]:
        return i
    else:
        return -1

print(search_rotated_array([4,5,6,1,2,3],3))
