#author : Amol Ambkar
# python program
# to access value of
# key which is
# not present in dict
# by setting default value
# using get

a = {
    "name":"tech blooded",
    "year":2021
}

b = a.get("type","education")
# as type key is not
# in dict a
# it will return 
# education

print(b)
