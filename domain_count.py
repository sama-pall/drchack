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
    ln = pieces[1].split('@')
    dm = ln[1]
    counts[dm] = counts.get(dm, 0) + 1

print(counts)

