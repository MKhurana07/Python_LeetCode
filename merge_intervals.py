def merge_intervals(num):
    num.sort()
    lenght= len(num)-1
    i=0
    while i< lenght:
        val = num[i]
        val2=num[i+1]
        if val[1] >= val2[0]:
            num[i+1] = [val[0],max(val2[1],val[1])]
            del num[i]
            lenght-=1
        i+=1

    return num
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
