def rotated_arr_search(num, val):
    #num.sorted()
    for i in range(len(num)):
        if num[i] < num[i-1]:
            start = i
    print(start)
    if val <= num[0] and val >= num[start]:
        return search(num[start:],val)
    elif val >= num[0] and val <= num[start-1]:
        return search(num[:start],val)
    return False

def search(num,val):
    l = 0
    r = len(num)-1
    mid = (l+r)//2
    print(num[mid])
    while l<=r:
        if val == num[mid]:
            return True
        elif val> num[mid]:
            l = mid+1
        elif val < num[mid]:
            r = mid-1
        mid = (l+r)//2
    return False

if True == rotated_arr_search([2,3,4,7,0,1],1): print("hello")
##def rotated_arr_search_2(num, val):
##    for i in range(len(num)):
##        if val < num[i]:
##            continue
##        if num[i] < num[i-1] and val >num[i]:
##            return False
##        elif num[i] 
