

def isPalindrome(n):
    return n == n[::-1]
    # we are finding the reverse of the string 
    # and checkong if the reverse and the original are same or not.
print(isPalindrome("racecar"))

# new method

def isPalindrome1(n):
    j=-1
    flag=0
    # compares the first and last element of the string and give the rest of the substring
    # to a recursive call to itself
    for i in n:
        if i!= n[j]:
            j = j -1
            flag = 1
            break
        j = j -1
    if flag ==1:
        print(" Not a Palindrome")
    else:
        print("Is a Palindrome")

isPalindrome1("Radar")