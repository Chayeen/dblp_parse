# dblp_parse
First, this project parses dblp xml files and outputs articles with their important properties, including journal or conference, title, page number, year, URL.

And then it picks up journals and conferences in ccf list.

Finally, it provides a simple interface to users for searching their interesting articles by filter keywords in title.

# Preface
Because of the file size limitations (25M), the source data file (__dblp.xml__, 2.1G, which can be received from http://dblp.uni-trier.de/xml/), the output file of dblpparse.py (__after2000all.txt__, 557M) and the output file of filterccf.py (__intreccf.txt__, 25M) don't be uploaded. However, you can run this code in order as README.md says to receive these files.

In this project, dblp.dtd and dblp.xml.gz were downloaded at Jan 18, 2018. You can receive these newest source data files from http://dblp.uni-trier.de/xml/.

# File Specification
1. __dblp.dtd and dblp.xml__: received from http://dblp.uni-trier.de/xml/, which are provided by dblp official and updated each month.
2. __dblpparse.py__: Its input files are __dblp.dtd and dblp.xml__. They should be in a same folder. Its function is to parse the source data file and to output all articles with their important properties after 2000. Its output file is __after2000all.txt__, which includes articles properties, such as  journal or conference, title, page number, year, URL.
3. __ccflist.csv__: Based on the ccf list from http://www.ccf.org.cn/xspj/gyml/, I choose the topic Computer Network and the topic Network and Information security by filtering these conferences and journals to pick important and relevant articles.
4. __filterccf.py__: Its input files are __ccflist.csv and after2000all.txt__. Its function is to filter articles which are in ccflist.csv. Its output file is __intreccf.txt__.
5. __filtercontent.py__: Its input file is __intreccf.txt__. Its function is to filter articles by searching one keyword in title or the year of articles. It provides an interface to receive keyword and year as parameters. Its output file name format is "keyword_year.csv", e.g. "DNS_2017.csv". The command is just like `python3 filtercontent.py DNS,2017`.
6. __DNS.sh__: It's a script for receiving articles in several years. Its input file is __filtercontent.py__. Its function is to receiving articles which keyword is "DNS" and year interval is from 2000 to 2017. Its output file is __DNSafter2000all.csv__
7. __DNSafter2000all.csv__: It's the final output file, including all recomended articles to read.

dblp.dtd & dblp.xml -> dblpparse.py ->after2000all.txt

ccflist.csv & after2000all.txt -> filterccf.py -> intreccf.txt

intreccf.txt -> filtercontent.py -> keyword_year.csv

filtercontent.py -> DNS.sh -> DNSafter2000all.csv

# Experiment
Support Python3.

# Command
`python3 filtercontent.py DNS,2017`
You can replace keyword "DNS" to any one word. Don't support serveral keywords now.