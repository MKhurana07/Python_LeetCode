def jump(num):
    jump,pos = 0,0
    while pos < len(num)-1:
        if num[pos+1] > num[pos]:
            pos = pos +1
            jump = jump +1
        elif num[pos+1] < num[pos]:
            pos = pos + num[pos]
            jump = jump +1
    return jump

print(jump([4,3,1,1,4,5]))
            
