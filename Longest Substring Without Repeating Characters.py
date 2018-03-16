def lengthOfLongestSubstring(s):
        temp =''
        prev_len = 0
        for i in s:
            if i not in temp:
                temp = temp + i
                if len(temp) > prev_len:
                    prev_len = len(temp)
            else:
                ind = temp.index(i) +1
                temp = temp[ind:]
                temp = temp + i
        return prev_len

def lengthOfLongestSubstring1(s): # This is better
        temp =''
        prev_len = 0
        for i in s:
            if i not in temp:
                temp = temp + i
            print(temp)
        return len(temp)

answer=lengthOfLongestSubstring("abcabcadefghi")
print(answer)
answer=lengthOfLongestSubstring1("abcabcadefghi")
print(answer)
