# python program to
# update existing set
# by keeping
# only common elements
# from both sets

set1 = {1,2,3}
set2 = {3,4,5,6}

set1.intersection_update(set2)

print(set1)
