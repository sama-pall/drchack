def main():
    l = input('Enter the line ')
    punt_check(l)
    if punt_check(l):
        print('Valid')
    else:
        print('Invalid')

def punt_check(s):
    for i in s[2:]:
        if i.isalpha():
            n = True
            continue
        elif i.isdigit():
            n = True
            continue
        else:
            if i.isalpha():
                n = False
                break

    return n


main()





#l = input('Enter the line ')
main()
