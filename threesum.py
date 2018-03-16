def threesum(nums):
    nums.sort()
    l = []
    for s in nums:
        for i in nums[nums.index(s) +1:]:
            for j in nums[nums.index(i)+1:]:
                if s+i+j ==0:
                    if [s,i,j] not in l:
                        l.append([s,i,j])
    return l
print(threesum([0,-1,-2,1]))

def find3sum(A, sum1): #Better Obv!!
 
    # Sort the elements 
    A.sort()
    arr_size =len(A)
    # Now fix the first element 
    # one by one and find the
    # other two elements
    res = []
    for i in range(0, arr_size-2):
     
 
        # To find the other two elements,
        # start two index variables from
        # two corners of the array and
        # move them toward each other
         
        # index of the first element
        # in the remaining elements
        l = i + 1
        
        # index of the last element
        r = arr_size-1
        while (l < r):
         
            if( A[i] + A[l] + A[r] == sum1):
                res = res + [[A[i]] + [A[l]] + [A[r]]]
                break
            elif (A[i] + A[l] + A[r] < sum1):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1
 
    # If we reach here, then
    # no triplet was found
    return res

print(find3sum([0,-1,2,1],3))
