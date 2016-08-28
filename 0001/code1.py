import random

#create list of characters to choose from
charList = map(chr, range(65, 91)) + map(chr, range(97, 123))
for i in range(0, 10):
    charList.append(str(i))

#randomly generate characters and check presence
code = []
for i in range(0, 200):
    token = ""
    for j in range(0, 20):
        digit = random.randint(0, 61)
        token = token + charList[digit]
    if (token in code) == True:
        i -=1
    else:
        code.append(token)

print code
