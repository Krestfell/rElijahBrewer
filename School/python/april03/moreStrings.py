def main():
    railrd = "PA Railroad"


def inOut():
    print(f'In & Out')
    searchString = 'Rail'
    if searchString in railrd:
        print(f'did not find {searchString} in {railrd}')
    else:
        print(f'found {searchString} in {railrd}')

    searchString = 'Road'
    if searchString in railrd:
        print(f'did not find {searchString} in {railrd}')
    else:
        print(f'found {searchString} in {railrd}')


def slices(railrd):
    print(f'now lets try slicing')
    print(f'{railrd[4:9]}')
    print(f'{railrd[0:12]}')
    print(f'{railrd[:12]}')
    print(f'{railrd[13:]}')


def basicStringOp(railrd):
    print(f'{railrd}')
    print(f'{len(railrd)}')
    searchString = 'Railroad'
    print(f'{railrd.find(searchString)}')
    searchString = 'PA'
    print(f'{railrd.find(searchString)}')

    print()
    for ch in railrd:
        print(ch, end='')
    print()

    print(railrd[0])
    print(railrd[-1])
    counter = len(railrd)-1
    backwards = ''
    while counter >= 0:
        backwards = railrd[counter]
        counter -= 1
    print(backwards)
