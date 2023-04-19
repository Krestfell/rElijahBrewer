# 1.1

def calculate_calories_from_fat(fat_grams):
    """Calculate the number of calories from fat."""
    return fat_grams * 9

def calculate_calories_from_carbs(carb_grams):
    """Calculate the number of calories from carbohydrates."""
    return carb_grams * 4

# 2.1

def gallons_of_paint(square_feet):
    """Calculates the number of gallons of paint required based on 112 square feet per gallon"""
    gallons = square_feet / 112
    return gallons

def hours_of_labor(square_feet):
    """Calculates the hours of labor required based on 112 square feet per gallon and 8 hours per gallon"""
    hours = (square_feet / 112) * 8
    return hours

def paint_cost(gallons, price_per_gallon):
    """Calculates the cost of the paint based on the number of gallons and the price per gallon"""
    cost = gallons * price_per_gallon
    return cost

def labor_cost(hours):
    """Calculates the cost of labor based on the hours required and the labor charge of $35 per hour"""
    cost = hours * 35
    return cost

def total_cost(paint_cost, labor_cost):
    """Calculates the total cost of the paint job"""
    total = paint_cost + labor_cost
    return total

# 3

def fallingDistance(t):
    g = 9.8
    d = 0.5 * g * t ** 2
    return d

for t in range(1, 11):
    distance = fallingDistance(t)
    print(f"After {t} seconds, the object has fallen {distance:.2f} meters.")

# 4

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(1, 10001):
    if isPrime(i):
        print(i)


def main():

    # 1.2

    # Get user input
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))

    # Calculate calories from fat and carbs
    calories_from_fat = calculate_calories_from_fat(fat_grams)
    calories_from_carbs = calculate_calories_from_carbs(carb_grams)

    # Display results
    print(f"Calories from fat: {calories_from_fat}")
    print(f"Calories from carbs: {calories_from_carbs}")

    #2.2

    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    price_per_gallon = float(input("Enter the price of paint per gallon: "))

    gallons = gallons_of_paint(square_feet)
    hours = hours_of_labor(square_feet)
    paint_cost_value = paint_cost(gallons, price_per_gallon)
    labor_cost_value = labor_cost(hours)
    total_cost_value = total_cost(paint_cost_value, labor_cost_value)

    print(f"\nGallons of paint required: {gallons:.2f}")
    print(f"Hours of labor required: {hours:.2f}")
    print(f"Cost of the paint: ${paint_cost_value:.2f}")
    print(f"Labor charges: ${labor_cost_value:.2f}")
    print(f"Total cost of the paint job: ${total_cost_value:.2f}")


if __name__ == "__main__":
    main()
