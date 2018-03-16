def longestPrefix(l):
    l.sort()
    i=0
    prefix = ''
    for char in l[len(l)-1]:
        if char == l[0][i]:
            prefix = prefix + char
            i= i+1
    return prefix

print(longestPrefix(['tedest','teeth','teemp','teel']))

def longestCommonPrefix( strs):
        if not strs:
            return ""
        
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
        
print(longestCommonPrefix(['tedest','teeth','teemp','teel']))
