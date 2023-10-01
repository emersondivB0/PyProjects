"""_summary_
- Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
- The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
- The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
- After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file name: ")
fh = open(fname)
dct = dict()
lstfull = list()
for line in fh:
    if line.startswith("From "):
        lst = line.split()
        lstfull += lst
        dct[lst[1]] = 1
for i in dct:
    dct[i] = lstfull.count(i)
    
maxv = 0
for j in dct:
    if dct[j] > maxv:
        maxv = dct[j]
        maxk = j

print(maxk,maxv)
