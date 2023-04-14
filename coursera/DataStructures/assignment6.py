"""_summary_
- Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
- You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
- From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
- Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
handle = open(name)
dct = dict()
lstfull = list()
for line in handle:
    if line.startswith("From "):
        lst = line.split()
        pos = line.find(':')
        time = line[pos-2:pos+6]
        timelist = time.split(":")
        lstfull.append(timelist[0])
        print(timelist)
        dct[timelist[0]] = 1
for i in dct:
    dct[i] = lstfull.count(i)
    final = list()

dicf = dict(sorted(dct.items()))

for clave, valor in dicf.items():
    print(clave, valor)
