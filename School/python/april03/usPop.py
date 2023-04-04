def main():
    print('')

    with open(r"C:\Users\heyit\Desktop\Projects\GitHub\rElijahBrewer\School\python\april03\USPopulation.txt") as file:
        pop_list = [int(line.strip()) for line in file.readlines()]

    # calculate the annual change in population
    annual_change = [(pop_list[i+1] - pop_list[i]) /
                     1000 for i in range(len(pop_list)-1)]

    # calculate the average annual change
    avg_annual_change = sum(annual_change) / len(annual_change)
    print("Average Annual Change in Population: {:.2f} thousand".format(
        avg_annual_change))

    # find the year with the greatest increase in population
    max_increase_year = annual_change.index(max(annual_change)) + 1951
    print("Year with Greatest Increase in Population: {}".format(max_increase_year))

    # find the year with the smallest increase in population
    min_increase_year = annual_change.index(min(annual_change)) + 1951
    print("Year with Smallest Increase in Population: {}".format(min_increase_year))

    print('')


if __name__ == '__main__':
    main()
