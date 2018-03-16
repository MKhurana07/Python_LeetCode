def AddBinary(a,b):
    dec_a = toDec(a)
    dec_b = toDec(b)
    print(dec_a,dec_b)
    add = dec_a + dec_b
    return toBin(add)

def toDec(a):
    dec = 0
    for i,val in enumerate(a):
        if val !=0:
            print(i,val)
            dec = dec + int(val)*pow(2,i)
    return int(dec)

def toBin(a):
    if a==0:
        return str(0)
    else:
        return toBin(a//2) + str(a%2)

print(AddBinary("11","1"))
            
            
