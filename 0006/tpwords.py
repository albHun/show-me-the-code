def findTop(fileName):

    top_num = 100
    
    #create 2d word list
    wlist = []
    wlist.append([])
    wlist.append([])
    poplist = []
    poplist.append([])
    poplist.append([])
        
    #open file and read data
    fhand = open(fileName)
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
    
    #put the 50 most frequent words into poplist
    fw = zip(wlist[1], wlist[0])
    fw.sort()
    fw.reverse()
    wlist[0] = [w for f, w in fw]
    wlist[1] = [f for f, w in fw]

    poplist[0] = wlist[0][:top_num]
    poplist[1] = wlist[1][:top_num]
    return poplist    
