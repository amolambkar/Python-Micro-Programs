# python program
# to convert dictionary
# to string and
# then back to
# dictionary

d = {
    "Name":"Tech Blooded",
    "Year":2021
}

import json
s = json.dumps(d)
print(s)
print(type(s))

a = json.loads(s)
print(a)

print(type(a))