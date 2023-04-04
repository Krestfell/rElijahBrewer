def main():
    # Loop over numbers from 1 to 99 (excluding 100)
    for x in range(1, 100):
        # Call getAliquot function with each number as argument
        getAliquot(x)


def getAliquot(num):
    # Initialize abundantTxt variable to 'Deficit'
    abundantTxt = 'Deficit'
    # Initialize summary variable to 0
    summary = 0

    # Get all factors of the number using the getFactors function
    factors = getFactors(num)

    # Calculate the sum of all factors (excluding the number itself)
    for summ in factors:
        summary += summ
    summary -= num

    # Check if the number is a prime
    if summary == 1:
        abundantTxt = 'Prime'
    # Check if the number is abundant
    if summary > num:
        abundantTxt = 'Abundant'
    # Check if the number is perfect
    if summary == num:
        abundantTxt = 'Perfect'

    # Print the number, factor count, all factors, Aliquot, and abundance classification
    print(f'{num} Factor Count: {len(factors)} {factors} Aliquot: {summary} {abundantTxt}')


def getFactors(num):
    # Initialize an empty list to store factors
    ret = []
    # Loop over all numbers from 1 to the number itself (inclusive)
    for i in range(1, num + 1):
        # Check if the number is a factor of the given number
        if num % i == 0:
            # Append the factor to the list of factors
            ret.append(i)
    # Return the list of factors
    return ret


if __name__ == '__main__':
    # Call the main function
    main()
