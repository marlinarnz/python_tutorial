# here you find the solutionsd for the Exercises
# keep in mind: there is not only one solution, so if your code does not look exactly the same, but delivers similar
# solutions its fine :)

# Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2
print("Exercise 1:")
# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)
# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)

# Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number,
# and In each iteration print the sum of the current number and previous number
def sumNum(num):
# for-loop might be useful
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum, " Sum: ", sum)
        previousNum = i
print("Exercise 2:")
print("Printing current and previous number sum in a given range(10)")
sumNum(10)

# Exercise 3: Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string
def removeChars(str,n):
  return str[n:]
print("Exercise 3:")
print("The new string is:")
print(removeChars("transportmodelling",9))
# what do you have to change to get the first 7 characters?
# change return str[n:] to return str[:n]
def removeChars(str,n):
  return str[:n]
print(removeChars("transportmodelling",9))

# Exercise 4: Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
sampleList = [34, 54, 67, 89, 11, 43, 94]
print("Exercise 4:")
print("Original list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)
sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)
sampleList.append(element)
print("List after Adding element at last ", sampleList)

# Exercise 5: Find out the index of 'age' of the given list
list1=['name', 'place of birth','age', 'town']
print('Exercise 5:')
print('age has the index:', list1.index('age'))

# Exercise 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def findDivisible(numberList):
    print("Exercise 6:")
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if (num % 5 == 0):
            print(num)
numList = [10, 20, 33, 46, 55]
findDivisible(numList)

# Exercise 7: Calculate income tax for the given income by adhering to the below rules
# first 10.000€ rate: 0%
# next 10.000€ rate: 10%
# remaining rate 20%
# test it with an income of 45.000€ (solution should be: 6.000€)
income = 45000
taxPayable = 0
print("Exercise 7:")
print("Given income", income, "€")
if income <= 10000:
    taxPayable = 0
elif income <= 20000:
    taxPayable = (income - 10000) * 10 / 100
else:
    # first 10,000
    taxPayable = 0
    # next 10,000
    taxPayable = 10000 * 10 / 100
    # remaining
    taxPayable += (income - 20000) * 20 / 100
print("Total tax to pay is", taxPayable, "€")

# Exercise 8: Take and print every second element of the list
mylist = [1, 2, 3, 4, 5, 6]
mylist = mylist[::2]
print('Exercise 8:')
print(mylist)

# Exercise 9: bring the list in the reverse order
mylist = [1, 2, 3, 4, 5, 6]
mylist.reverse()
print('Exercise 9:')
print(mylist)

#Exercise 10: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print('Exercise 10:')
print(list3)

#Exercise 11: create a list from the given one that replaces all numbers that are not divisible by 5 with 'NaN'
list1 = [4, 5, 8, 16, 15, 20, 24, 25, 44, 50]
myList = [var if var%5==0 else 'NaN' for var in list1]
print('Exercise 11:')
print(myList)

# Exercise 12: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
sampleDict = dict(zip(keys, values))
print('Exercise 12:')
print(sampleDict)

# Exercise 13: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print('Exercise 13:')
print(dict3)

# Exercise 14: Initialize dictionary with default values and access the individual data of 'Kelly'
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
resDict = dict.fromkeys(employees, defaults)
print('Exercise: 14:')
print(resDict)
# Individual data
print(resDict["Kelly"])

#Exercise 15: Delete set of keys from a dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary"]
sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
print('Exercise 15:')
print(sampleDict)

# Exercise 16: Get the key & value of a minimum value from the following dictionary
dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print('Exercise 16:')
print(min(dict, key=dict.get))
print('Minimum value:', min(dict.values()))

# Exercise 17: Add a list of elements to a given set
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print('Exercise 17:')
print(sampleSet)
# Note: Set is unordered.

# Exercise 18: Return a new set of identical items from a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print('Exercise 18:')
print(set1.intersection(set2))

# Exercise 19: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print('Exercise 19:')
print(set1.union(set2))

# Exercise 20: Check if two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print('Exercise 20:')
if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))

# Exercise 21: Check if all items in the following tuple are the same
def check(sampleTuple):
    return all(i == sampleTuple[0] for i in sampleTuple)
tuple1 = (45, 45, 45, 45)
print('Exercise 21:')
print(check(tuple1))