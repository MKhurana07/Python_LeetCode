def grayCode(n):    #space - O(n2)
    results = [0]
    for i in range(n):
        results += [x + pow(2, i) for x in reversed(results)]
    return results

print(grayCode(2))
    
