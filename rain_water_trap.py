##def trap(nums):
##    rain = 0
##    max_left = max_right= 0
##    for i in range(len(nums)):
##        if i > 0 and num[i]< num[i-1]:
##            max_left = max(num[i-1],max_left)
##            rain = rain + num[i-1]-num[i]
##        if num[i] == num[i-1] == 0:
##            rain = rain + 1
##        if num[i] > num[i-1]:
##            max_right = max(num[i],max_right)
##            rain = rain +1

            
def trap(height):
    n = len(height)
    l, r, water, minHeight = 0, n - 1, 0, 0
    while l < r:
        while l < r and height[l] <= minHeight:
            water += minHeight - height[l]
            l += 1
        while r > l and height[r] <= minHeight:
            water += minHeight - height[r]
            r -= 1
        minHeight = min(height[l], height[r])
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
