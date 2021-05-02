# program to check
# number is prime
# or not

n = int(input("num: "))

prime =False

if n > 1:
    for i in range(2,n):
        if n % i == 0:
            prime =True
            break

if prime:
    print("not prime")
else:
    print("prime")