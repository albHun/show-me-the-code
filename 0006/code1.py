import tpwords
import os, glob

# statistics list
staList = []
# word string
staList.append([])
# in how many texts the word apperead
staList.append([])
# how many times the word appeared
staList.append([])

# fill in the staList
for infile in glob.glob("./*.txt"):
    wlist = tpwords.findTop(infile)
    for word in wlist[0]:
        if word in staList[0]:
            staList[1][staList[0].index(word)] += 1
            staList[2][staList[0].index(word)] += wlist[1][wlist[0].index(word)]
        else:
            staList[0].append(word)
            staList[1].append(1)
            staList[2].append(wlist[1][wlist[0].index(word)])
            
# print keyword for each text
for infile in glob.glob("./*.txt"):
    wlist = tpwords.findTop(infile)
    for word in wlist[0]:
        if staList[1][staList[0].index(word)] <= len(glob.glob("./*.txt")) * 0.1:
            print infile.split('/')[-1].split('.')[-2], 'keyword:', word
            break
