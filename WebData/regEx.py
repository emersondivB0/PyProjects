import re

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:"

x = re.findall('@(\S+)',data)
print(x)
