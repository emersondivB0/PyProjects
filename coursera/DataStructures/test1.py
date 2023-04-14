import random

x = random.randint(0,100)

print(x)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])
print(x.upper())

#data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#pos = data.find('.')
#print(data[pos:pos + 3])

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
y = text[pos:pos+6]
print(y)