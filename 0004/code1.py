fname = raw_input('Please enter file name:\n>')

#create 2d word list
wlist = []
wlist.append([])
wlist.append([])

#open file and read data
fhand = open(fname)
for line in fhand:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        if word in wlist[0]:
            wlist[1][wlist[0].index(word)] += 1
        else:
            wlist[0].append(word)
            wlist[1].append(1)  

#print
for i in range(len(wlist[0])):
    print 'Word', wlist[0][i], 'appeared', wlist[1][i], 'times.'

#print the 50 most frequent word
toplist = sorted(wlist[1])
toplist.reverse()
for i in range(50):
    print 'Word', wlist[0][wlist[1].index(toplist[i])], 'appeared', toplist[i], 'times.'

