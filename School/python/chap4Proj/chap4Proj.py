def main():
# 1

    print("Celsius\tFahrenheit")
    print("-------------------")
    for celsius in range(0, 31):
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}\t{fahrenheit:.1f}")

    print('')
    
# 2

    grains_per_square = 1
    total_grains = 0
    total_bushels = 0
    total_dollars = 0
    
    # create table header
    print("{:<10s} {:<20s} {:<15s} {:<15s}".format(
        "Square", "Grains of Rice", "Bushels", "Dollar Amount"))
    
    # loop over each square and calculate number of grains, bushels, and dollars
    for square in range(1, 65):
        grains_on_square = grains_per_square
        bushels_on_square = grains_on_square / 1305000
        dollars_on_square = bushels_on_square * 12.17
        
        # accumulate totals for each column
        total_grains += grains_on_square
        total_bushels += bushels_on_square
        total_dollars += dollars_on_square
        
        # print row for current square
        print("{:<10d} {:<20d} {:<15f} {:<15.2f}".format(
            square, grains_on_square, bushels_on_square, dollars_on_square))
        
        # double the number of grains for the next square
        grains_per_square *= 2
    
    # print totals row
    print("{:<10s} {:<20d} {:<15f} {:<15.2f}".format(
        "Total", total_grains, total_bushels, total_dollars))
    
    print('')
    
# 3

    rate = 1.6  # millimeters per year
    years = 25

    for year in range(1, years+1):
        rise = year * rate
        print(f"Year {year}: {rise:.2f} millimeters")

    print('')

# 4

    num = int(input("Enter a nonnegative integer: "))
    factorial = 1

    if num < 0:
        print("Error: You must enter a nonnegative integer.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            factorial *= i

        print(f"The factorial of {num} is {factorial}.")

if __name__ == "__main__":
    main()
