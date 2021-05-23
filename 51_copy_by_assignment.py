# when we use
# assignment operator
# to copy list
# then changes
# done in one list
# will automatically
# reflect in other
a = [1,2,3,4]
b = a
a.append(6)

print(a)
print(b)