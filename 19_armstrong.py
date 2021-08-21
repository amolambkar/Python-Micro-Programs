# Amol Ambkar
# program to check
# number is
# armstrong or not

n = int(input("num : "))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10

if n == sum:
    print("armstrong")
else:
    print("not an armstrong")
