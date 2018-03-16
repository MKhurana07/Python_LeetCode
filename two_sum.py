def twoSum(nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if(sum==target):
                    
                    print(i,j)
twoSum([0,1,2,3],3)

def twoSum2(nums, target): #This one is better!!
        answ_dic = {}
        ans =[]
        for i,val in enumerate(nums):
                leftover = target - val
                if leftover in answ_dic:
                        ans= ans + [[answ_dic[leftover], i]]
                else:
                        answ_dic[val] = i
        return ans
print(twoSum2([0,1,2,3],3))
