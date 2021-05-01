# program to
# find factorial
# of number

n = int(input("Enter the number"))

if n < 0:
    print("factorial does not exists for number less than 0")
elif n == 0:
    print("factorial for 0 is 1")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    
    print("factorial of given number is",fact)