import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    pieces = line.split()
    wd = pieces[1]
    counts[wd] = counts.get(wd, 0) + 1
bigc = None
for word in counts:
    value = counts[word]
    if bigc is None or value > bigc:
        bigw = word
        bigc = value

print(bigw, bigc)
