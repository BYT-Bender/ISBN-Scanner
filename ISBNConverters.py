def ISBN10toISBN13(ISBN10):
    # See https://isbn-information.com/convert-isbn-10-to-isbn-13.html
    ISBN10 //= 10
    ISBN10 += 978000000000
    l = [int(_) for _ in str(ISBN10)]

    checkDigit = 38 # 9*1 + 7*3 + 8*1 = 9 + 21 + 8 = 38
    for i in range(3, len(l)) :
        if i % 2 == 0 :
            checkDigit += l[i]
        else :
            checkDigit += l[i] * 3
        print(i, l[i], 3*l[i], checkDigit)
    
    ISBN10 *= 10
    
    f = lambda x : x + 10 - checkDigit%10 if checkDigit%10 else x

    # if checkDigit % 10 :    # Pythonic way of doing True-False. (0 = false, everything else is true)
    #     ISBN10 += 10 - checkDigit%10
    # else :
    #     continue    # No need to add zero to the number.

    return f(ISBN10)

def ISBN13toISBN10(ISBN13):
    # https://freeisbn.com/isbn-converter/
    ISBN13 -= 9780000000000
    ISBN13 //= 10

    weight, checkDigit, i = 2, 0, 0
    l = [int(_) for _ in str(ISBN13)][::-1]
    
    for i in range(8) :
        checkDigit += l[i] * weight
        weight += 1
        i += 1

    ISBN13 *= 10
    
    f = lambda x : x + 11 - checkDigit%11 if checkDigit%11 else x

    return f(ISBN13)
