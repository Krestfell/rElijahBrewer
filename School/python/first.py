def mpg():
    miles = int(input("Enter miles driven: "))
    gallons_used = int(input("Enter gallons used: "))
    mpg = miles / gallons_used
    print(miles, " / ", gallons_used, " = ", mpg, " mpg ")


def temperature():
    celsius = int(input("Enter degrees Celsius: "))
    fahr = (celsius * 9/5) + 32
    print("Celsius ", celsius, " converted to Fahrenheit ", fahr)


def vines():
    row_length = int(input("Enter row length in feet: "))
    row_space = int(input("Enter space between rows: "))
    gap = int(input("Enter the gap between vines: "))
    vines = row_length - 2 * row_space / gap
    print("Row length: ", row_length, end=" ")
    print("Row space: ", row_space, end=" ")
    print("Gap between vines: ", gap, end=" ")
    print("Number of vines: ", vines)


mpg()
temperature()
vines()
