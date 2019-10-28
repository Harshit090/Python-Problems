def palindrome(a):
    b = a[::-1]
    if b == a:
        return True
    else:
        return False


a = input("Enter a string to be checked for palindrome\n")
c = palindrome(a)

if c == True:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
