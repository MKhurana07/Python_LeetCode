def isScramble1(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2): # prunning
        return False
    for i in range(1, len(s1)):
        if (isScramble1(s1[:i], s2[:i]) and isScramble1(s1[i:], s2[i:])) or (isScramble1(s1[:i], s2[-i:]) and isScramble1(s1[i:], s2[:-i])):
            return True
    return False

print(isScramble1("great","rgtae"))
