

def isPalindrome(n):
    return n == n[::-1]
    # we are finding the reverse of the string 
    # and checkong if the reverse and the original are same or not.
print(isPalindrome("racecar"))