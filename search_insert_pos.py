def Search_insert_position(nums,val):
    for i in range(0,len(nums)):
        if val > nums[i] and val < nums[i+1]:
            return i+1
        elif val == nums[i]:
            return i

print(Search_insert_position([1,2,4,5],2))
        
