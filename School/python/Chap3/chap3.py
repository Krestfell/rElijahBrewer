import math


def main():
    # 1) User Input

    num = int(input("Enter an integer: "))
    print(f"{num} is {'even' if num % 2 == 0 else 'odd'}.")

    # 2) Ask A Number

    num = input("Enter a number from 1-7: ")
    # Check if input is a valid integer in the range of 1-7
    if num.isdigit() and 1 <= int(num) <= 7:
        # Display corresponding day of the week
        if num == "1":
            print("Monday")
        elif num == "2":
            print("Tuesday")
        elif num == "3":
            print("Wednesday")
        elif num == "4":
            print("Thursday")
        elif num == "5":
            print("Friday")
        elif num == "6":
            print("Saturday")
        elif num == "7":
            print("Sunday")
    else:
        # Display error message if input is invalid
        print("Invalid input. Please enter a number from 1-7.")

    # 3) Length & Width

    # Get the length and width of the first rectangle
    length1 = float(input("Enter the length of rectangle 1: "))
    width1 = float(input("Enter the width of rectangle 1: "))

    # Calculate the area and diagonal length of rectangle 1
    area1 = length1 * width1
    diagonal1 = math.sqrt(length1**2 + width1**2)

    # Get the length and width of the second rectangle
    length2 = float(input("Enter the length of rectangle 2: "))
    width2 = float(input("Enter the width of rectangle 2: "))

    # Calculate the area and diagonal length of rectangle 2
    area2 = length2 * width2
    diagonal2 = math.sqrt(length2**2 + width2**2)

    # Compare the areas of the two rectangles
    if area1 > area2:
        print("Rectangle 1 has the greater area.")
    elif area2 > area1:
        print("Rectangle 2 has the greater area.")
    else:
        print("The two rectangles have the same area.")

    # Compare the diagonal lengths of the two rectangles
    if diagonal1 > diagonal2:
        print("Rectangle 1 has the greater diagonal length.")
    elif diagonal2 > diagonal1:
        print("Rectangle 2 has the greater diagonal length.")
    else:
        print("The two rectangles have the same diagonal length.")

    # 5) Hot Dog Party

    HOT_DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8
    HOT_DOGS_PRICE_PER_PACKAGE = 3.49
    BUNS_PRICE_PER_PACKAGE = 2.59
    BEER_PRICE = 5.98

    # Get the number of people attending the cookout and the number of hot dogs per person
    num_people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(
        input("Enter the number of hot dogs each person will be given: ")
    )

    # Calculate the number of hot dogs and buns needed
    total_hot_dogs_needed = num_people * hot_dogs_per_person
    hot_dog_packages_needed = total_hot_dogs_needed // HOT_DOGS_PER_PACKAGE
    if total_hot_dogs_needed % HOT_DOGS_PER_PACKAGE != 0:
        hot_dog_packages_needed += 1

    total_buns_needed = num_people * hot_dogs_per_person
    bun_packages_needed = total_buns_needed // BUNS_PER_PACKAGE
    if total_buns_needed % BUNS_PER_PACKAGE != 0:
        bun_packages_needed += 1

    # Calculate the number of hot dogs and buns left over
    hot_dogs_leftover = (
        hot_dog_packages_needed * HOT_DOGS_PER_PACKAGE
    ) - total_hot_dogs_needed
    buns_leftover = (bun_packages_needed * BUNS_PER_PACKAGE) - total_buns_needed

    # Calculate the total cost
    hot_dogs_cost = hot_dog_packages_needed * HOT_DOGS_PRICE_PER_PACKAGE
    buns_cost = bun_packages_needed * BUNS_PRICE_PER_PACKAGE
    total_cost = hot_dogs_cost + buns_cost + BEER_PRICE

    # Print the results
    print(f"Minimum number of packages of hot dogs required: {hot_dog_packages_needed}")
    print(f"Minimum number of packages of hot dog buns required: {bun_packages_needed}")
    print(f"Number of hot dogs left over: {hot_dogs_leftover}")
    print(f"Number of hot dog buns left over: {buns_leftover}")
    print(f"Total price for hot dogs: ${hot_dogs_cost:.2f}")
    print(f"Total price for hot dog buns: ${buns_cost:.2f}")
    print(
        f"Total cost for hot dogs, hot dog buns, and a sixer of Bud: ${total_cost:.2f}"
    )


if __name__ == "__main__":
    main()
