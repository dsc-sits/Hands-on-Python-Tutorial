# printing statements

print("hello world")

#printing multiple statements

print("""
hello world
how are you?
wassup?""")

# VARIABLES

firstName = "shivani"
lastName = "Ghadigaonkar"

# assigning multiple value to multiple variables

fname, lname, rollno = "shivani", "Ghadigaonkar", 40
print(fname)
print(lname)
print(rollno)

# assigning same value to multiple variables

a = b = c = 30
print(a)
print(b)
print(c)

# LIST

a = [1, 2.2, 'python']
print(a)
# adding element to a list

a.append("javaScript")
print(a)

# removing elements from a list

a.remove(a[0])
print(a)

a.remove("javaScript")
print(a)

# Inserting element in a particular position

a.insert(1,"Java")
print(a)

# Extending the list

b = [1,2,3]
a.extend(b)
print(a)

# slicing

print(a[0])
print(a[1:3])
print(a[-1])
print(a[::-1])

# list of list

list1 = [[1,3],[1,4],[6]]
print(list1[2][0])
list1.append((5,6))
print(list1)


#TUPLE

t = (1,2,3)
s = (2,3,4)


print(t+s)

print(list1*3)

print(list(t))
print(tuple(list1))

# DICTIONARY

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict1['Name'])
print("dict['Age']: ", dict1['Age'])

# updating the Dictionaries

dict1['Age'] = 8; # update existing entry
dict1['School'] = "DPS School"; # Add new entry

print("dict['Age']: ", dict1['Age'])
print("dict['School']: ", dict1['School'])

#  function dict()

Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

# LOOPS

list4 = [1, 2, 3, 4, 5]

for num in list4:
  print(num)
# sum1 = 0
# for num in list4:
# 	sum1 = sum1 + num
# print(sum1)
# while loop

int i = len(list4)
while(i<0):
  print(list4[i])
  i = i-1

# IF STATEMENT
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


# FUNCTION

def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	return("Hello, " + name + ". Good morning!")


# EXCEPTION HANDLING

import sys

print( "Lets fix the previous code with exception handling")

try:
     number = int(input("Enter a number between 1 - 10 "))

except ValueError:
     print( "Err.. numbers only")
    
 
finally:
 	print( "you entered number ", number)

#regEX

import re
# matches()
pattern = '^a...s$'
test_string = "abyss"
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")


# findall()


string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# split()

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

#sub()

# multiline string

string = 'abc 12\
de 23 \n f45 6'
pattern = '\s+'
replace = '$'
new_string = re.sub(pattern, replace, string) 
print(new_string)

# subn()

# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = '$'

new_string = re.subn(pattern, replace, string) 
print(new_string)

# search()

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found") 

