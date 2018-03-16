def Combo(nums, target):
    res = []
    nums.sort()
    
    dfs(nums, target, 0, [], res)
    return res

def dfs(nums, target, index, path, res):
    if target <0:
        return
    if target == 0:
        res.append(path)
    else:
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                dfs(nums,target-nums[i],i+1,path + [nums[i]],res)

print(Combo([2,3,4,6,7],7))
