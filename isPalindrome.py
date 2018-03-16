def isPalindrome(x):
    if (x<0 or x%10==0):
        return false
    real_x = x
    reverse = 0
    while(x>0):
        reverse = reverse*10 + x%10
        x= int(x/10)
        
    return real_x == reverse

print(isPalindrome(123421))

def checkispalindrome(string):
    b = string[::-1]
    if b == string:
        return True
    else:
        return False
        
