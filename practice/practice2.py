#list []

subway = ['Kim', 'Ahn', 'Chu']

print(subway)
print(subway.index('Kim'))

subway.append("Lee")
print(subway)

# pop() substitues the last element
subway.pop()
print(subway)

subway.pop()
print(subway)

subway.append("Chu")
subway.append('Lee')
subway.append('Han')
subway.append('Kim')
print(subway)

# count the elements in the list
print(subway.count('Kim'))

# sorting lists, sort() make lists in ascending.
num_list = [5,1,2,4,0,3]

num_list.sort()
print(num_list)

# reverse() make lists in descending.
num_list.reverse()
print(num_list)

'''
# erase all
num_list.clear()
print(num_list)

'''

# extend() adds a list behind another one.

num_list.extend(subway)
print(num_list)

# library {}
cabinet = {3:'Kim', 100:"Lee"}
print(cabinet)

print(cabinet[3]) # when there is no key value in the library like 5, 10 etc, it occurs an error message.
print(cabinet.get(3)) # when there is no key value in the library, it occurs just 'None' instead of the error message.
print(cabinet.get(5, "valuable key")) # you can add a message which will be shown, when there is no key value in the library.

# True and False
print(3 in cabinet)
print(5 in cabinet)


boxes = {"a-3": "Kim", "b-5": "Lee", "a-14": "Chu"}

print(boxes)
boxes['a-3'] = 'Ahn' # be replaced
boxes["a-14"] = 'Han' # be replaced
print(boxes)

# Delete key and value.
del boxes['a-3']
print(boxes)

# print only keys
print(boxes.keys())

# print only values
print(boxes.values())

# print keys and values
print(boxes.items())

# clear all
print(boxes.clear())
print(boxes)

# (): tuple quicker than list. but any value can not be added and changed.

menu = ('escalope', 'frite')
print(menu)
print(menu[0])
print(menu[1])

'''
menu.add("filet de boef")
add function can not be applied to the tuple.'''

(name, age, hobby) = ('Chu', '37', 'coding')
print(name, age, hobby)
print(age)

# set. it does not sort the set in descending or ascending order. It does not like repeated values.

my_set = {1,2,3,4,4,4,4,5}
print(my_set) # it gives only 1,2,3,4,5

like_apple = {"Han", "Chu", "Kim"}
like_peach = {"Han", "Chu"}
like_banana = set( ["Han", "Ahn", "Go"] )

# intersection, 'and' oerator "&" or intersection()
print(like_apple & like_banana)
print(like_apple & like_peach)
print(like_apple.intersection(like_peach))

# union, 'or' operator "|" or union()
print(like_banana | like_peach)
print(like_banana.union(like_peach))

# different set substraction operator '-' or difference()
print(like_apple - like_banana)
print(like_apple.difference(like_banana))

# you can add to the set. you can remove.
print(like_apple.add("Nho")) # why does it give 'None'
print(like_apple)

print(like_apple.remove("Nho"))
print(like_apple)


# set can be changed in class into list, tuple and back to set.

carte_dessert = {"cafe au lait", "une boule de glace", "gateaux"}

print(carte_dessert)
print(type(carte_dessert))  # set

carte_dessert = list(carte_dessert)
print(carte_dessert, type(carte_dessert))  # list

carte_dessert = tuple(carte_dessert)
print(carte_dessert, type(carte_dessert))  # tuple

carte_dessert = set(carte_dessert)
print(carte_dessert,type(carte_dessert))  # set

'''
Q3) There is a coding competition in your school.
We prepare an online comment event to raise the attendence rate.
We are going to give gifts one person for a fried chicken, there for coffee coupons.
make a code to draw for winners.

condition 1: there are 20 comments. Let their IDs 1~20.
condition 2: randomly choose. and not repeated.
condition 3: use 'shuffle' and 'sample' functions out of 'random module'.

ex)

-- winners --
chicken : 1
coffee : [2,3,4]
-- congratulation --

'''

participants = list(range(1,21))

from random import *
winner1 = sample(participants,1)
participants.remove(winner1[0])
shuffle(participants)
winner2 = participants[0:3]

print("-- winners --\nchicken: " + str(winner1[0]) + "\ncoffee: "+ str(winner2)+ "\n-- congratulation --")
