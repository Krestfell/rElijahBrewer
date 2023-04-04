import matplotlib.pyplot as plt
import csv
import random


def main():
    firstGraph()


def firstGraph():
    x = []
    y = []

    with open('sales.txt', 'r') as csvFile:
        plots = csv.reader(csvFile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(random.randint(2000, 10000))

    plt.plot(x, label='Sales')
    plt.plot(y, label='Random')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sales')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
