import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# URL assignment http://py4e-data.dr-chuck.net/comments_1761896.xml
# URL test http://py4e-data.dr-chuck.net/comments_42.xml


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter url: ')


html = urllib.request.urlopen(address, context=ctx).read()

tree = ET.fromstring(html)
# lst = stuff.findall('users/user')

numbers = tree.findall(".//comment/count")

sum = 0
for number in numbers:
    sum += int(number.text)
print(sum)