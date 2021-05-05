# program to remove
# punctuations from
# string

#define punctuations
punc ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

s = "Hello !!,this is tech.."

no_punc = ""
for c in s:
    if c not in punc:
        no_punc += c

print(no_punc)