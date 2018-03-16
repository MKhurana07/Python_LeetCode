def lettercombs(digits):
    diction = {1:(),'2':['a','b','c'],'3':['d','e','f'],4:('g','h','i'),5:('j','k','l'),6:('m','n','o'),7:('p','q','r'),8:('t','u','v'),9:('w','x','y','z'),0:()}
    result=[]
    for s in str(digits):
        if result == []:
            result.append(diction[s])
        else:
            for i in result and for j in diction[s]:
                result.append(result[i]*diction[s][j])
            #result.append(diction[s]*result)
    return result
print(lettercombs(23))
    
