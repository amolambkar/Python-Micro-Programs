# program to
# take
# matrix input

row = 2
col = 3

m = []

for i in range(row):
    a = []
    for i in range(col):
        a.append(int(input()))
    m.append(a)

print(m)