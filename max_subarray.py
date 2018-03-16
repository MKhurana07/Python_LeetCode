def max_subarray(num):
    if not num:
        return 0
    curr_sum = max_sum = num[0]
    for i in num[1:]:
        curr_sum = max(i,curr_sum + i)
        max_sum = max(curr_sum, max_sum)
    return max_sum


print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
