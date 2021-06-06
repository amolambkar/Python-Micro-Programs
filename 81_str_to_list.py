# python program
# to convert list to
# string
# and then back to
# list

import json

l = ["tech","blooded"]

s = json.dumps(l)
print(s)
print(type(s))

a = json.loads(s)
print(a)
print(type(a))