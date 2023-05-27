import re

hand = open('mbox.txt')
reg = input('Enter a regular expression:')
count = 0 
for line in hand:
    line = line.rstrip()
    if re.search(reg, line):
        count +=1
    else: pass
print(count)

  
