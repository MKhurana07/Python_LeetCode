def isValid(s):
    dict = {'{':'}',"(":")","[":"]"}
    flag = 0
    for char in s:
        try:
            if char in dict.keys():
                if s[s.index(char) +1] == dict[char]:
                    flag = 1
                    s= s[s.index(char)+2:]
                else:
                    flag = 0
        except:
                flag = 0
    return flag

print(isValid('{}()[]'))
