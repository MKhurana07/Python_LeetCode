def longestPalindrome(s):
    prev_len = 0
    temp = ''
    for i in s:
        if i not in temp:
            temp = temp + i
            if len(temp) > prev_len:
                prev_len = len(temp)
        else:
            temp = temp +i
            answer = check(temp)
            if answer == 0 and len(temp) >prev_len:
                print("here")
                prev_len = len(temp)
                temp = ''
    return prev_len

def check(st):
    if len(st) ==1:
        return 0
    elif st[:1] == st[-1:]:
        check(st[1:len(st)-2])
        return 0
    else:
        return 1
       
print(longestPalindrome("helehog"))

def longestPalindrome1(s,beg,end): # BEst answer!!!!! DP
    if beg == end:
        return 1
    if s[beg]==s[end] and beg+1==end:
        return 2
    if s[beg]==s[end]:
        return longestPalindrome1(s,beg+1,end-1) + 2
    return max(longestPalindrome1(s,beg,end-1),longestPalindrome1(s,beg+1,end))    
    

print(longestPalindrome1("cbbd",0,3))
