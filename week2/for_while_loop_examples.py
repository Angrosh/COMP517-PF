# def add(x, y):
#      return x+y

# def mult(x, y):
#     return x*y
    


# result = add(2, 3)
# print('result', result)

# multipy = mult(2, 3)
# print('multiply', multipy)


# dataList = [0, 1, 2, 3]
# j = 0
# while j < len(dataList):
#     print(dataList[j])
#     j = j+1


# ## infinite loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1


""" # break: break the closest enclosing loop
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')
 """


# names = ['Sam', 'Tom', 'Jack']
# j = 0
# while j < len(names):
#     if names[j] == 'Sam':
#         print(names[j])
#         break
#     j += 1


# ## continue: go the start of the closest enclosing loop
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         print()
#         continue
#     print(n)
# print('Loop ended.')


# ## while-else loop
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Loop done.')


# ## looping through a list
# a = ['foo', 'bar', 'baz', 'qux']
# s = 'bar'

# i = 0
# while i < len(a):
#     if a[i] == s:
#         # Processing for item found
#         print('item found')
#         print(i)
#         break
#     i += 1
# else:
#     # Processing for item not found
#     print(s, 'not found in list.')


# ## ask for user input
# countFrom = int(input("Please give me a start number: "))
# countTo = int(input("Please give me a finish number: "))

# print(countFrom, countTo)

# for _ in range(countFrom, countTo):
#     print(_)
#     print("Another interation...")

# a = ['foo', 'bar', 'baz', 'qux']
# s = 'bar'
# for item in a:
#     print(item)


# ## Number of Items in basket
# numItems = int(input("How many items do you have? "))

# #Total price
# totalPrice = 0.0

# for i in range(0, numItems):
#     #Price of item i
#     price = float(input("Enter the price of Item " + str(i) + ": "))
#     totalPrice = totalPrice + price

# #Total price
# print("Total Price is: £{:.2f}".format(totalPrice))

# print(numItems)
# # Python 2.7
# for key, value in sampleDict.iteritems():
#     print(key, value)

# # Python 3
# for key, value in sampleDict.items():
#     print(key, value)


# sampleDict = {'text_1': ['Title', 'keywords', 'content']}

# ## iterate through dictionary - key
# sampleDict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for key in sampleDict:
#     print(key)


# ## iterate through dictionary - key, value
# sampleDict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for key, value in sampleDict.items():
#     print(key, value)


# ## iterate through dictionary - (key, value) tuple
# sampleDict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for item in sampleDict.items():
#     print(item)


# ## invert keys and values - example 1
# sampleDict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# newDict = {}
# for key, value in sampleDict.items():
#     print(value)


# ## invert keys and values - example 1
# sampleDict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# newDict = {}
# for key, value in sampleDict.items():
#     newDict[value] = key
# print(newDict)


# ## invert keys and values - example 2
# sampleDict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# newDict = {v: k for k, v in sampleDict.items()}
# print(newDict)


# ## Filtering items in a dictionary - example 1
# sampleDict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# newDict = {}  # Create a new empty dictionary
# for key, value in sampleDict.items():
#     # If value satisfies the condition, then store it in new_dict
#     if value == 2:
#         newDict[key] = value
# print(newDict)

# ## Filtering items in a dictionary - example 2
# sampleDict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# newDict = {k: v for k, v in sampleDict.items() if v == 2}
# print(newDict)


# ## sorted by keys
# productCost = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# for key in sorted(productCost):
#     print(key, '->', productCost[key])


# productCost = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# sortedDict = {k: v for k, v in sorted(productCost.items(), key=lambda item: item[1])}
# print(sortedDict)

# lambda expressions
# lambda p1, p2 : expression
# lambda x, y : x+y

# add = lambda x, y : x+y
# print(add(1, 2))


## nested if/elif/else condition
age = 25
gender = 'M'

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')    



# lamda functions are anonymous functions
# without a name
#print(lambda x, y : x+y(1, 2))



