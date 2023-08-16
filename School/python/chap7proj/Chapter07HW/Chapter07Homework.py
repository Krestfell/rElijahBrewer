#Chapter07Homework.py

def main():
      #chargeAccountValidate()
      #nameFinder()
      population_data()

      
def population_data():
      summary = 0
      year = 1950
      population_list = fileToList("USPopulation.txt")
      for i in population_list[1]:
            summary += int(i)
            year += 1
      print(f'Summary {summary}')
      print(f'Average: {summary / int(population_list[0])}')
      print(f'Max: {max(population_list[1])}')
      print(f'Min: {min(population_list[1])}')



def nameFinder():
      #Alexis
      #Pedro
      testName = input("Enter name to search: ")
      girlsNames = boysNames = allNames = []
      fileName = 'GirlNames.txt'
      girlsNames = fileToList(fileName)[1]
      boysNames = fileToList('BoyNames.txt')[1]
      allNames = girlsNames + boysNames
      for x in allNames:
            if x == testName:
                  print(f'Found {testName}')
            else:
                  print(f'{testName} Not Found')
                  break
      


def fileToList(fileName):
      returnList = []
      counter = 0
      try:
            infile = open(fileName)
            for line in infile:
                  returnList.append(line.rstrip())
                  counter += 1
            infile.close()

      except IOError:
            print("An error occured whilst reading the file")
      except:
            print("An error occured")
      else:
            return counter, returnList






def chargeAccountValidate():
      #8777541
      testAccount = input('Enter the charge accound number: ')
      testList = []
      try:
            infile = open('charge_accounts.txt', 'r')
            for line in infile:
                  testList.append(line.rstrip())
            infile.close()
      except IOError:
            print("An error occured whilst reading the file")
      except:
            print("An error occured")
      else:
            print("Done")
      lineCounter = 0
      for x in testList:
            lineCounter += 1
            if x == testAccount:
                  print(f"Found:{x} at line number: {lineCounter}")
                  break
      


      



if __name__ == '__main__':
      main()
