def sort_colors_dutch(nums):
    red = white = 0
    blue = len(nums)-1
    while (white <= blue):
        if nums[white] == 1:
            white = white + 1
        elif nums[white] == 0:
            nums[white]=nums[red]
            nums[red]=0
            white = white +1
            red = red + 1
        else:
            nums[white] = nums[blue]
            nums[blue] =2
            blue = blue -1
    return nums

print([1,1,2,0,0,2,1,0,2])
