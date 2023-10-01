filename = input("Enter the file name: ")
filehandle = open(filename, 'r')
leer = filehandle.read()
leer = leer.rstrip()
print(leer.upper())
count = 0
for line in filehandle:
    if line.startswith("P"):
        count += 1
print(count)