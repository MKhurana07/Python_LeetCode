def permutation(num):
    l = []
    if len(num)  ==0:
        return
    if len(num) ==1:
        return [num]
    for i in range(len(num)):
        m = num[i]
        
        rest = num[:i] + num[i+1:]
        for p in permutation(rest) :
           l.append([m] + p)
    return set(l)

print(permutation([2,1,3]))
