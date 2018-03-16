def Combination_sum_rept(num, target):
    answer = []
    for i in num:
        if i == target:
            answer.append(i)
    answer.append(Combination_sum_rept2(num, target,answer))
    return answer

def Combination_sum_rept2(num, target,answer):
    left = 1
    test = []
    for i in num:
        test.append(i)
        left = target - i
        if (left >0):
            test.append(Combination_sum_rept2(num, left,answer))
        if left == 0:
            answer.append(test)
    return answer

#print(Combination_sum_rept([2,3,6,7],7))
   

def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs( nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)            

print(combinationSum([2,3,6,7],7))
