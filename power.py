def Pow(x,n):
    if n<0:
        x = 1/x
        n=-n
    pow = 1.000
    for i in range(0,n):
        pow= pow*x
    return pow
    

print(Pow(2.000,-2))
