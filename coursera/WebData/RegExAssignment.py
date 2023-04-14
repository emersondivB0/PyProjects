import re

archivo = open('./regex_sum_1761892.txt', 'r')
contenido = archivo.read()
archivo.close()
x = re.findall('[0-9]+', contenido)
sum = 0
for i in x:
    sum += int(i)

print(sum)
