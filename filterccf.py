import csv
import pdb


# conflist = []
conflist = {}
with open("ccflist.csv","r") as csvfiler:
    read = csv.reader(csvfiler)
    for line in read:
        if not line:
            break
        # conflist.append(line[0])
        conflist[line[0]] = 0


wfile = open("intreccf.txt","w")
file = open('after2000all.txt', 'r')
for line in file:
    if not line:
        break
    first = line.index('/')
    second = line.index('/',first+1)
    conf = line[:second+1]
    # if conf in conflist:
    if conf in conflist.keys():
        conflist[conf] += 1
        wfile.write(line)
        # print(line,end='')
    # pdb.set_trace()
file.close()
wfile.close()

for conf in conflist.keys():
    print(conf,conflist[conf])