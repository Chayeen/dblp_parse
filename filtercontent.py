import sys
import pdb
import csv

if len(sys.argv) == 1:
    filterstring = "DNS,2017"
elif len(sys.argv) == 2:
    filterstring = sys.argv[1]
else:
    print("input error!")
    sys.exit(0)

tmp = filterstring.split(",")
filterkeyword = tmp[0]
filteryear = tmp[1]
print(filterkeyword,filteryear)

with open(filterkeyword+"_"+filteryear+".csv","w") as csvfiler:
    read = csv.writer(csvfiler)
    file = open('intreccf.txt', 'r')
    for line in file:
        if not line:
            break
        tmp = line.split(";,;")
        if len(tmp) <= 4:
            # print(line)
            continue
        key = tmp[0]
        title = tmp[1]
        pages = tmp[2]
        year = tmp[3]
        ee = tmp[4]
        if title.find(filterkeyword) >= 0 and year == filteryear:
            # pdb.set_trace()
            # print(key+","+title+","+pages+","+year+","+ee)
            read.writerow([title,year,key,pages,ee])