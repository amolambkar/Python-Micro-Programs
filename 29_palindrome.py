# program to
# check
# string is
# palindrome or not

s = input("string : ")

s1 = reversed(s)

if list(s) == list(s1):
    print("Palindrome")
else:
    print("Not Palindrome")