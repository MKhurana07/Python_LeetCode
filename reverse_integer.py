def reverse(integer):
    s=1
    if integer <0:
        s=-1
        integer = s*integer
    x = str(integer)
    rev =''
    for i in range(0,len(x)):
        rev= rev + x[-1:]
        x = x[:-1]
    return s*int(rev)
print(reverse(-1220))

def reverse1(integer): #This is better!
    s=1
    if integer <0:
        s=-1
    x = str(integer*s)
    x=x[::-1]
    x= int(x)
    ans= s*x
    return ans if ans.bit_length() <32 else 0
print(reverse1(-12883938393983893839888888938939839839893889389389398398398320))
