fhand = open('words.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])    
