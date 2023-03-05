def count(w,l):
    word = 'banana'
    count = 0
    for i in w:
        if i == l:
            count = count + 1
    print(count)


w = input('Word is: ')
l = input('Letter you are looking for is :')
print(w.count(l))
#count(w,l)
