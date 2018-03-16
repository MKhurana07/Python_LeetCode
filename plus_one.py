def plus_one(num):
    flag = 1
    for i in num:
        if i != 9:
            flag = 0
    if flag == 1:
        num[0] = 1
        for i in range(1,len(num)):
            num[i]=0
        num.append(0)
    return num


def plusone(num):
    number = 0
    for digit in num:
        number = number*10 + digit
    return [int(i) for i in str(number+1)]

            
print(plusone([9,9]))
