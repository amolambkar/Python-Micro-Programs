# Author - Amol Ambkar

# program to
# find
# factors of given
# number

n = int(input("n: "))

for i in range(1,n+1):
    if n%i == 0:
        print(i)
