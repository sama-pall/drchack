while True:
    _ = input('Fraction :').strip()
    #_ = _.strip()

    try:
        x, y = _.split('/')
        if x < y:
            x = int(x)
            y = int(y)
            fr = (100*x/y)
    except ValueError:
        print('Doesn\'t look like integer numbers, try one more time')
    except ZeroDivisionError:
        print('Volume can\'t be 0, try one more time')
    else:
        break

if fr <= 1:
    print('E')
elif 99 <= fr <= 100:
    print('F')
else:
    print('{:.0f}'.format(fr)+'%')
