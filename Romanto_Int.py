def RomantoInt(num):
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    result = 0
    for i in range(0,len(num)-1):
        if romans[num[i]] < romans[num[i+1]]:
            result = result - romans[num[i]]
        else:
            result = result + romans[num[i]]
        
    return result + romans[num[len(num)-1]]
print(RomantoInt("MCMI"))
