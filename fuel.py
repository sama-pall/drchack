while True:
    _ = input('Fraction :').strip()
    #_ = _.strip()
    x, y = _.split('/')
    if x < y:
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print('Doesn\'t look like integer numbers, try one more time')
        else:
            break


try:
    fr = (100*x/y)
except ZeroDivisionError:
    print('Volume can\'t be 0, try one more time')
else:


    if fr <= 1:
        print('E')
    elif 99 <= fr <= 100:
        print('F')
    else:
        print('{:.0f}'.format(fr)+'%')
