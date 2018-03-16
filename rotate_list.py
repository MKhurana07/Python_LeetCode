def rotate_list(num,k):
    result = num[k:] + num[:k]
    return result

print(rotate_list([1,2,3,4,5],2))
