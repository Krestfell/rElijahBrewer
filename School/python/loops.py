import math


def main():
    print(' ')
    """

    # while loop
    print("while")
    counter = 0
    while counter < 10:
        print(f'{counter}', end=' ')
        counter += 1
    print()

    # pseudo do loop
    print(f 'do loop fakery')
    counter = 0
    while (True):
        if counter >= 10:
            break
        print(counter, end=' ')
        counter += 1
    print()

    # for loop
    print("for")
    for num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(num, end=' ')
    print()

    print("for range")
    for num in range(5, 55,):
        print(num, end=' ')
    print()

    # nested
    print("nested")
    for num in range(10, 20):
        for exponent in range(1, 6):
            print(f'{num} ^ {exponent} = {num ** exponent}')

    for num in range(1, 21):
        print(f'{num} squared {num ** 2.0}')

    string = 'jeff is a wizard.'
    for x in string:
        print(x, end = '')
    print()

    collection = ['jeff', 5, 'wizard']
    for x in collection:
        print(type(x), end = '')
    print()

    """

    '''

    # Sentinel value for loop control
    print("let's work with mean: ")
    counter = 0
    totVal = 0
    while (True):
        tempVal = int(input('Enter a positive integer, -99 to quit '))
        if tempVal == -99:
            if counter != 0:
                print(f 'average is {totVal / counter}')
            else:
                print('no average to calculate')
            break
        totVal += tempVal
        counter += 1

    '''

    '''

    for i in range(1, 40):
        jugglers(3)

    print('collatz:')
    for i in range(1, 30):
        collatz(i)

    '''
    print(help(tempConversion))
    for counter in range(-40, 100, 5):
        print(f'{counter} -> {tempConversions[counter]}')


def factorial(number):
    # Factorial
    print('factorial')
    if num < 0:
        return -1
    if num == 0:
        return 1
    myFact = 1
    count = 1
    while count <= num:
        myFact = myFact * count
        count = count + 1
    return myFact


def tempConversion(celsius):
    # calc from f to c
    print('temp conversion')
    return 9/5.0 * celsius + 32


def tideChange(year):
    # calc rising tide at 1.6 mm per year
    print('tide change')
    rise = 1.6
    for counter in range(0, year+1)


def jugglers(counter):
    # print('jugglers')
    while counter > 1:
        print('{:,}'.format(counter), end=' ')
        if counter % 2 == 0:
            factor = .5
        else:
            factor = 1.5
        counter = math.floor(counter ** factor)
    print(1)


def collatz(compareNumber):
    # \n collatz(number)
    # Return list of Collatz Conjecture sequence for a single number
    while compareNumber > 1:
        print(compareNumber, end=' ')
        if compareNumber % 2 == 0:
            compareNumber = math.floor(compareNumber / 2)
        else:
            compareNumber = math.floor(3.0*compareNumber + 1)
    print(1, end='\n\n')


if __name__ == '__main__':
    main()
