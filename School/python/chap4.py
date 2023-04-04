# Assignment
'''Chessboards have 64 squares. Write a program that would place one grain of rice on the first square, two grains on the second square, four grains on the third square and continue the doubling until all 64 squares have been covered. Given that there are 1,305,000 grains of rice in a bushel and $12.17 per bushel, produce a table that shows the square number, the number of grains of rice, the number of bushels on each square and the dollar amount of that squares rice.  The program will need to show a total for each column of the total.'''

# Constants
squares = 64
grainsPerBush = 1305000
pricePerBush = 12.17

# Initialization
grains = 1
totalGrains = 0
totalBushels = 0
totalPrice = 0
