def threesum(nums,tar):
    nums.sort()
    l = {}
    lis=[]
    for s in nums:
        for i in nums[nums.index(s) +1:]:
            for j in nums[nums.index(i)+1:]:
                l[(tar-(s+i+j))]= [s,i,j]
    lis = sorted(l.keys())
    return l[lis[0]]
print(threesum([0,-1,-2,1],1))



def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        answ = [num[0],nums[1],nums[2]]
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == target:
                    return sum
                
                if abs(target - sum) < abs(result - target):
                    result = sum
                    answ = [nums[i],nums[k],nums[j]]
                
                if sum < target:
                    j += 1
                else:
                    k -= 1
        
        return answ, result

print(threesum([-1,2,1,-4],1))
