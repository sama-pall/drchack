

while True:   
    try:
        fname = input('Enter your file name: ')
        fstr = open(fname)
    except FileNotFoundError:
        print('Wrong file name, try one more time')
    else:
        break
    
if fname.strip() != 'na na boo boo':
    
    count = 0
    spam_s = 0 
    for i in fstr:
    #number of spam lines
        i = i.rstrip()
        if i.startswith('X-DSPAM-Confidence:'):
            count = count +1
            #counting numbers after whitespace
            num = float(i[i.find(' '):])
            spam_s = spam_s + num
    print('Average spam confidence:', spam_s/count)
else:
    print(fname.upper(),'TO YOU - You have been punk\'d ')
            
        

