# python program to 
# reverse the
# sentence

a = input("sentence : ")

words = a.split(' ')

out = ' '.join(\
    reversed(words))

print(out)