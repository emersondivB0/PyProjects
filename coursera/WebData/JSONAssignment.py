import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

'''
Write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1761897.json (Sum ends with 32)
'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Get the url
address = input('Enter url: ')
#Reading the data
data = urllib.request.urlopen(address, context=ctx).read()

info = json.loads(data)
lst = info['comments']
print(len(lst))

sum = 0
for item in lst:
    for i in item:
        sum += int(item['count'])
        
print(int(sum/2))