import random


def main():
    writeFile()
    appendFile()
    readFileByFile()
    readFileByLine()
    readLoop()
    writeFileBinary()
    readWith()
    writeWith()


def writeFile():
    print("Writing file")
    with open('sales.txt', 'w') as outputFile:
        # Use a list comprehension to generate random numbers and write them to file
        outputFile.writelines(
            [str(random.randrange(1, 10001)) + "\n" for count in range(10)])


def appendFile():
    with open('sales.txt', 'a') as outputFile:
        # Use a list comprehension to generate random numbers and write them to file
        outputFile.writelines(
            [str(random.randrange(1, 10001)) + "\n" for count in range(10)])
    print('sales.txt appended')


def readFileByFile():
    print('readFileByFile')
    with open('sales.txt', 'r') as infile:
        # Use read() to read the entire file as a string
        contents = infile.read()
        print(type(contents))
        print(contents)


def readFileByLine():
    print('readFileByLine')
    with open('sales.txt', 'r') as infile:
        # Use read lines() to read the file into a list of lines
        content = infile.readlines()
        print(type(content))
        sum = 0
        for line in content:
            # Use strip() to remove whitespace characters, including the newline at the end of each line
            sum += int(line.strip())
        print(f'the sum is {sum}')


def readLoop():
    print('readLoop')
    with open('sales.txt', 'r') as infile:
        for line in infile:
            # Use strip() to remove whitespace characters, including the newline at the end of each line
            print(line.strip())


def writeFileBinary():
    print('Writing binary file')
    byteArr = [120, 3, 255, 0, 100]
    binaryFormat = bytearray(byteArr)
    with open('salesB.bin', 'w+b') as outputFile:
        # Use write() to write the byte array to the binary file
        outputFile.write(binaryFormat)


def readWith():
    with open('sales.txt', 'r') as file:
        data = file.read()
        print(data)


def writeWith():
    with open('sales.txt', 'a') as file:
        # Use a list comprehension to generate random negative numbers and write them to file
        file.writelines(
            [str(random.randrange(1, 10001) * -1) + '\n' for count in range(10000)])


if __name__ == '__main__':
    main()
