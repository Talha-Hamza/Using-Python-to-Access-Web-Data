import re
data = open('actual.txt')
numlist = list()
for line in data:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    for num in number:
        numlist.append(int(num))
print(sum(numlist))

