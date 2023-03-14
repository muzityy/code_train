def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True
    else:
        s = str(x)
        return s == s[::-1]
