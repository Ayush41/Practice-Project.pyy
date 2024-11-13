def is_palindrome(s):
    s = s.replace(" ","").lower()

    return s == s[::-1]

userInput = input("Enter anything")

if is_palindrome(userInput):
    print("This is a palindrome")
else:
    print("This is not a palindrome")