#Chapter 07 Lists and Tuples.py

import random

def main():

      print('\n\nTuple Time')
      tuple1 = (1, 3, 5, 7)
      print(f'len(tuple1) {type(type1)}')
      print(f'len(tuple1) {len(tuple1)}')
      for x in range(len(tuple1)):
            print(f'{x} {tuple1[x]}')

      length = len(tuple1)
      print(f'{tuple[0:length]}')
      print(f'Len: {len(tuple1)} Max: {max(tuple1)} Min: {min(tuple1)}')

      singleValueTuple = (50,)
      print(singleValueTuple)

      print(tuple1[0])

      tuple2 = tuple1 + singleValueTuple
      print(f'Len: {len(tuple2)} Max: {max(tuple2)} Min: {min(tuple2)}')
      print(tuple2)

      student_tuples = [('jon', 'A', 32),
                              ('dave', 'B', 25),
                              ('bacon', 'F', 18),]
      








      

      print(f"Even numbers and a list")
      even_numbers = [2, 4, 6, 8, 10]
      print(f'{type(even_numbers)} {even_numbers}')

      print(f'\n List of several different data type')
      info = ['Jon', 99, 3.14159]
      print(f'{type(info)} {info}')

      for i in range(len(info)):
            print(f'{type(info[i])} {info[i]}')

      print(f'Create a list of 5 numbers using range command')
      numbers = list(range(5))
      print(f'{type(numbers)} length: {len(numbers)} {numbers}')

      print(f'List using range(1, 10, 2)')
      numbers = list(range(1, 10, 2))
      print(f'{numbers}')

      print(f'List using [0] * 5 \n{[0] * 5}')
      print(numbers)

      print(f'Change first element to 15 using numbers[0] = 15 ')
      numbers[0] = 15
      print(numbers)

      list1 = [1, 3, 5, 7]
      list2 = [2, 4, 6, 8]
      list3 = list1 + list2

      print(f'Let\'s add(concatenate) two lists together')
      print(f'{list1} + {list2} = {list3}')
      print(f'Temporary sort(used sorted):\n {list1} + {list2} = {sorted(list3)}')
      print(f'list3 has not been permanent sorted')
      print(f'{list1} + {list2} = {list3}')
      print(f'To permanently sort a list uses list3.sort() mehod {list3.sort()}')
      print(f'{list3}')
      print(f'list.sort() only works for Lists, sorted() works for any iterable')


      print(f'One way to create a list: squares.append(x**2) in a for loop')
      squares = []
      for x in range(10):
            squares.append(x**2)
      print(squares)

      print(f'Another way is to use "squares = [x**2 for x in range(10)]"')
      squares = [x**2 for x in range(10)] #List Comprehension
      print(squares)

      print('List Slicing')

      days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
      sunday = days[0]
      friday = days[5]
      print(f'{sunday} and {friday}')
      mid_days = days[2:5]
      print(f'days[2:5] {mid_days}')

      print('n\nMore Lists')
      names = ['Angela', 'Richard', 'Razanne', 'Eric', 'Isaac', 'Janet', 'Tasha', 'Griffon', 'Jonathan',
               'Jacob', 'Gregory', 'Felicity', 'Carlos', 'Jacob', 'Sergio']
      print(names[0:4])
      print(names[-1])
      print(names[-3:-1])

      search = 'Angela'
      if search in names:
            print(search, ' was found')
      else:
            print(search, ' was not found')

      names.append("Mathew")
      names.append("Mark")
      names.append("Lucas")
      print(names)

      for i in names:
            print(i)

      names.insert(0, 'Billy')
      names.insert(1, 'Stew')
      names.insert(2, 'George')
      names.insert(0, 'Django')
      print(names)

      names.sort()
      print(names)
      names.remove('Stew')
      print(names)
      names.remove('Jacob')
      print(names)

      names.reverse()
      print(names)

      print(f'The minimum value of names: {min(names)}')
      print(f'The maximum value of names: {max(names)}')
      print()

      names2 = names
      print(names2)
      print()

      names2.reverse()
      print(f'1) {names}')
      print(f'2) {names2}')

      names2 = []
      for item in names:
            names2.append(item)

      names2.reverse()
      print(f'1) {names}')
      print(f'2) {names2}')
      print()
      print(f'pop([i]) return and removes the ith element of list, \ no i means last element')
      print(f'names.pop() = {names.pop()}')
      print(f'{names}')
      print(f'names.pop(5) = {names.pop(5)}')
      print(f'{names}')

      two_dimensional()
      three_dimensional()
      four_dimensional()

def two_dimensional():
    """
        This function demonstrates 2 dimensional lists
    """    
    print("\nTwo dimensional")
    calories = [[ 'Sunday', 500, 800, 900],
                      [ 'Monday', 550, 850, 950],
                      [ 'Tuesday', 600, 900, 1000],
                      [ 'Wednesday', 650, 950, 1050],
                      [ 'Thursday', 450, 750, 850],
                      [ 'Friday', 400, 700, 800],
                      [ 'Saturday', 350, 800, 1100]]

    for day in range(len(calories)):
        for meal in range(len(calories[day])):
            print(calories[day][meal], end=' ')
        print()



def three_dimensional():
    """
    This function demonstrates 3 dimensional lists
    """
    print("\nThree Dimensional")
    calories = [['week1',[ 'Sunday', 500, 800, 900],
                                   [ 'Monday', 550, 850, 950],
                                   [ 'Tuesday', 600,900,1000],
                                   [ 'Wednesday', 650,950,1050],
                                   [ 'Thursday', 450,750, 850],
                                   [ 'Friday', 400,700,800],
                                   [ 'Saturday', 350,800,1100]],
                      ['week2',['Sunday', 500, 800, 902],
                                   [ 'Monday', 550, 850, 952],
                                   [ 'Tuesday', 600,900,1002],
                                   [ 'Wednesday', 650,950,1052],
                                   [ 'Thursday', 450,750, 852],
                                   [ 'Friday', 400,700,802],
                                   [ 'Saturday', 350,800,1102]],]
    for week in range(len(calories)):
        for day in range(len(calories[week])):
            for meal in range(len(calories[week][day])):
                print(calories[week][day][meal], end=' ')
            print()
        print() 



def four_dimensional():
    """
    This function demonstrates 4 dimensional lists
    """
    print("\nFour Dimensional")
    calories = [['January',['week1',[ 'Sunday', 500, 800, 900],
                 [ 'Monday', 550, 850, 950],
                 [ 'Tuesday', 600,900,1000],
                 [ 'Wednesday', 650,950,1050],
                 [ 'Thursday', 450,750, 850],
                 [ 'Friday', 400,700,800],
                 [ 'Saturday', 350,800,1100]],
                ['week2', ['Sunday', 500, 800, 902],
                 [ 'Monday', 550, 850, 952],
                 [ 'Tuesday', 600,900,1002],
                 [ 'Wednesday', 650,950,1052],
                 [ 'Thursday', 450,750, 852],
                 [ 'Friday', 400,700,802],
                 [ 'Saturday', 350,800,1102]],
                ['week3', ['Sunday', 500, 800, 903],
                 [ 'Monday', 550, 850, 953],
                 [ 'Tuesday', 600,900,1003],
                 [ 'Wednesday', 650,950,1053],
                 [ 'Thursday', 450,750, 853],
                 [ 'Friday', 400,700,803],
                 [ 'Saturday', 350,800,1103]],
                ['week4',['Sunday', 500, 800, 904],
                 [ 'Monday', 550, 850, 954],
                 [ 'Tuesday', 600,900,1004],
                 [ 'Wednesday', 650,950,1054],
                 [ 'Thursday', 450,750, 854],
                 [ 'Friday', 400,700,804],
                 [ 'Saturday', 350,800,1104]]],
               ['February',['week1',[ 'Sunday', 500, 800, 900],
                 [ 'Monday', 550, 850, 950],
                 [ 'Tuesday', 600,900,1000],
                 [ 'Wednesday', 650,950,1050],
                 [ 'Thursday', 450,750, 850],
                 [ 'Friday', 400,700,800],
                 [ 'Saturday', 350,800,1100]],
                ['week2', ['Sunday', 500, 800, 902],
                 [ 'Monday', 550, 850, 952],
                 [ 'Tuesday', 600,900,1002],
                 [ 'Wednesday', 650,950,1052],
                 [ 'Thursday', 450,750, 852],
                 [ 'Friday', 400,700,802],
                 [ 'Saturday', 350,800,1102]],
                ['week3', ['Sunday', 500, 800, 903],
                 [ 'Monday', 550, 850, 953],
                 [ 'Tuesday', 600,900,1003],
                 [ 'Wednesday', 650,950,1053],
                 [ 'Thursday', 450,750, 853],
                 [ 'Friday', 400,700,803],
                 [ 'Saturday', 350,800,1103]],
                ['week4',['Sunday', 500, 800, 904],
                 [ 'Monday', 550, 850, 954],
                 [ 'Tuesday', 600,900,1004],
                 [ 'Wednesday', 650,950,1054],
                 [ 'Thursday', 450,750, 854],
                 [ 'Friday', 400,700,804],
                 [ 'Saturday', 350,800,1104]]],
               ]

    for month in range(len(calories)):
        for week in range(len(calories[month])):
            for day in range(len(calories[month][week])):
                for meal in range(len(calories[month][week][day])):
                    print(calories[month][week][day][meal], end=' ')
                print()
            print()
    
      















if __name__ == '__main__':
      main()
