import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Function to get the specific name and url
def names_dict(x):
    html = urllib.request.urlopen(x, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    hlink = tags[17].get('href', None)
    name = hlink.split('/')[-1].split('_')[2].split('.')[0]
    return name,hlink
    
#loop to get into de urls 
i=1
while i <= 7:
    name,url = names_dict(url)
    i += 1
    
print(name)    