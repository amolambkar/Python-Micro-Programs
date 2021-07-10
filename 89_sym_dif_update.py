# python program
# to keep only
# elements those are 
# not common in
# two sets

a = {1,2,3}
b = {3,4,5}

a.symmetric_difference_update(b)

print(a)
