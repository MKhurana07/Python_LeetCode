def steal_values(num):
    choose={}
    for i in range(len(num)):
        val = num[i]
        if i>0 and i <len(num)-1 and val > num[i+1] + num[i-1]:
            choose[i] = val
        elif i ==0 and val > num[i+1]:
            choose[i] = val
        elif i == len(num)-1 and val > num[i-1]:
            choose[i] = val
        i = i +2
    sum=0
    for i in choose:sum = sum + choose[i]
    return sum
print(steal_values([6,2,3,7]))
        
