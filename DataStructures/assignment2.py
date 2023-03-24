"""_summary_
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
         X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
val = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        pos = line.find('0')
        val += float(line[pos:pos+6])
        continue
average = val/count
print("Average spam confdence: ", average)