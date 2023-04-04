def main():
    divide_by_zero()
    sales_report()


def sales_report():
    total = 0.0  # initialize an accumulator

    try:
        with open('sales.txt', 'r') as infile:  # use 'with' statement for file handling
            header_line = next(infile)  # skip the header line
            for line in infile:
                amount = float(line.strip())
                total += amount
        print(f"Total sales: {total:,.2f}")

    except IOError:
        print("Error: Couldn't read sales.txt file.")
    except ValueError:
        print("Error: Non-numeric data found in sales.txt.")
    except Exception as e:  # catch all other exceptions and print the error message
        print(f"Error: {e}")


def divide_by_zero():
    z = 100
    for i in range(-10, 10):
        try:
            result = z / i
            print(i, z / i)
        except ZeroDivisionError as err:
            print(err)


if __name__ == '__main__':
    main()
