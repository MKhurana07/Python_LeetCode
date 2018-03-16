def subsets(num):
    res=[[]]
    for i in num:
        res = res + [item+[i] for item in res]
    return res

def subsets_withDup(S):
    res = [[]]
    S.sort()
    for i in range(len(S)):
        if i == 0 or S[i] != S[i - 1]:
            l = len(res)
        for j in range(len(res) - l, len(res)):
            res.append(res[j] + [S[i]])
    return res

print(subsets([1,2,3]))
print(subsets_withDup([1,2,2])) 
    
