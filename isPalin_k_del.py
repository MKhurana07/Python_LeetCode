def isPalindrome_k_del(nums, k):
    reverse = nums[::-1]
    length = len(nums)

    return (isKPal(nums, reverse,length, length) <= k)

def isKPal(str1, str2, len1, len2):
    if not len1:
        return len2
    if not len2:
        return len1
    if str1[len1-1] == str2[len2-1]:
        return isKPal(str1,str2,len1-1,len2-1)
    res = 1 + min(isKPal(str1,str2, len1-1,len2),isKPal(str1,str2,len1,len2-1))
    return res

print(isPalindrome_k_del("abcbd",2))
