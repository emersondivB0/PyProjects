import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
numbers = soup.find_all(text=re.compile('[0-9]+'))

for number in numbers:
    try:
        sum += int(number)
    except ValueError:
        pass


print(sum)