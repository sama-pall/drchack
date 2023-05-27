import re

hand = open('mbox-short.txt')
count = s =  0 
for line in hand:
    line = line.rstrip()
    x= re.findall('New Revision: ([\d]+)', line)#look for string with numbers, return only numbers
    if len(x) > 0:
        count +=1
        s = s + int(x[0])
print(int(s/count))#counts & return average

  
