# let's see how much i remember of python lol

### STRINGS


message = "Hello World" # or could be 'Hello World', i like to use '' for chars and "" for more than 1 char

# multi-line strings - uses 3 quotation marks
longMessage = """Hello World
How are you?"""  #would print as two separate lines

# can grab one character from string using []
message[1] # returns index 1 of string message, 'e'

# can slice strings using [:]
message[2:5] # returns string from 2nd index (inclusive) to 5th index (exclusive)

# .lower() method - returns the string object calling .lower() in all lowercase
message.lower() #returns  "hello world"

# .upper() method - returns the string object calling .upper() in all uppercase
message.upper() #returns "HELLO WORLD"

# .count(string) method - returns the number of times the 'string' argument is found in the object calling .count()
message.count('l') #returns 3

# .find(string) method - returns the index of the first instance where 'string' argument is found in the object calling .find()
message.find('World') #returns 6

# .replace(stringToReplace, replacementString) - returns a copy of the object calling .replace() w the string in 1st argument 
                                                                                # replaced by the string in the 2nd argument
message = message.replace("World", "Universe") #message would now equal "Hello Universe" - YOU MUST SET message to message.replace(),
                                                            #otherwise it will not change since message.replace creates a new string

# Concatenation and adding strings
greeting = "Hi"
name = "Fonz"
phrase = greeting + name #returns "HiFonz"
phrase = greeting + ", " + name #returns "Hi, Fonz"
# Formatted strings
phrase = "{}, {}, Welcome!".format(greeting, name) #returns "Hi, Fonz, Welcome!" - can also use ''.
# F strings - would recommend this for efficiency
phraseF = f"{greeting}, {name}, Welcome!" #returns "Hi, Fonz, Welcome!" - can also use '',
# can also call methods on the objects that are formatted into the string
phraseF = f"{greeting.lower()}, {name.upper()}, Welcome!" #returns "hi, FONZ, Welcome!"

###             DIR & HELP FUNCTIONS

#print(dir(name)) #returns list of methods you can call on an object
#print(help(str)) #returns list of methods you can call on datatype passed in argument, along with functionality details 
                    # only accepts datatypes as args
#print(help(str.lower)) #can also return functionality details for a specific method - have to pass it without ()

### INTEGERS, FLOATS, & MATH - NUMERIC DATA

# Division / - always returns a float (decimal)
3/6 # returns 0.5
# Floor Division // - returns an integer, rounds down
7//3 # returns 2
# Modulo % - returns an integer, remainder of first number divided by second number
4%3 # returns 1
# *= += -= /= - all ways of doing an operation and setting it to the variable
money = 4
money *= 2 # money would now equal 8

# abs(num) - returns absolute value of num
abs(-3) #returns 3

# round(num, numOfPlacesAfterDecimal) - rounds num up, depending on number of places after decimal (argument 2)
round(3.75) #returns 4
round(3.75, 1) #returns 3.8

# int(string) - casting strings to ints
num_1_string = "100" # 100 in string type
num_1 = int(num_1_string) #converting num_1_string to int and setting it equal to num_1

### LISTS, TUPLES, and SETS

# Lists & Tuples - sequential data
# Sets - unordred collections of values with no duplicates

## LISTS - mutable, can be changed

## creating lists - same thing as arrays
courses = [] # creates an empty list
courses = list() # also creates an empty list
courses = ["History", "Math", "Physics", "CompSci"] # creates a list of strings

## accessing lists - similar to string slicing
courses[0] # returns "History"
courses[:2] # returns ["History", "Math"]
courses[2:] # returns ["Physics", "CompSci"]
courses[1:3] # returns ["Math", "Physics"]
courses[-1] # returns "CompSci" - indexes backwards
# attempting to access an index that doesn't exist ill give you an IndexError

## modifying lists

# .append(element) - appends element to end of list calling the method
courses.append("Art") # courses now has "Art" at end of list

# .insert(index, element) - inserts an element at index - same as append, but with a location
courses.insert(0, "Art") # inserts "Art" to 0th index of courses list
courses_2 = ["Art", "Education"]
courses.insert(0, courses_2) # inserts courses_2 list to 0th index of courses list - ["History", "Math", "Physics", "CompSci", ["Art", "Education"]]

# .extend(element) - inserts element to end of list calling the method - ideal for adding lists as an element
courses.extend(courses_2) # extends courses list to include each individual element of courses_2 list - ["History", "Math", "Physics", "CompSci", "Art", "Education"]

# .remove(element) - removes specific element from list calling method
courses.remove("Math") # removes "Math" element

# .pop() - removes and returns last element of list calling method
courses_2.pop() # removes "Education"
popped = courses_2.pop() # popped = "Education"

## sorting lists
courses = ["History", "Math", "Physics", "CompSci"]
nums = [1, 5, 2, 4, 3]

# .reverse() - reverses the elements in the list - last index to first
courses.reverse() # returns ["CompSci", "Physics", "Math", "History"]

# .sort() - returns elements in alphabetical order or ascending numerical order
courses.sort() # returns ["CompSci", "History", "Math", "Physics"]
nums.sort() # returns [1, 2, 3, 4, 5]
# .sort(reverse=True) - returns elements in reverse alphabetical order or descending numerical order
courses.sort(reverse=True) # returns ["CompSci", "Physics", "Math", "History"]

# sorted(list) - returns a sorted copy of list passed as argument, INSTEAD of mutating the list
sorted_courses = sorted(courses) # sorted_courses is sorted version of courses, courses remains unsorted

# min(list) - returns smallest element in list
min(nums) #returns 1

# max(list) - returns biggest element in list
max(nums) #returns 5

# sum(list) - returns sum of elements in list
sum(nums) #returns 15

## finding elements/values
courses = ["History", "Math", "Physics", "CompSci"]

# .index(element) - returns index where 1st instance of element is found in list calling method
courses.index("CompSci") #returns 3
# will get ValueError if element is not in list

# in operator - used to find if an element is in a list (bool)
"Art" in courses #returns false since "Art" is not in courses list
"CompSci" in courses #returns true

## looping through values in list

# for loops
    #"item" can be named anything its just a variable representing each item in courses
for item in courses:
    #print(item) # prints each item in courses list
    break

#can use enumerate to print out the index and the item, 
for index, course in enumerate(courses):
    #print(index, course) #prints each index and item i.e: 0 history, 1 math
    break

#can also pass a starting number for enumeration
for index, course in enumerate(courses, start=1):
    #print(index, course) #prints 1 history, 2 math
    break

## Separating / Joining Lists

# .join(list) - returns a string containing the values in the list passed as an argument seperated by whatever calls the .join() method
courses_str = ' - '.join(courses) # all the values in courses are placed into a string and separated by ' - ', set equal to courses_str

# .split(divider) - splits up the string calling the method wherever the divider is found, and returns a list with each split as an item
new_list = courses_str.split(' - ') # sets new_list equal to list of splits of courses_str at each ' - '

## Tuples - immutable, cannot change, cannot have items added, removed, or altered,

# creating tuples - uses () instead of []
courses_tuple = () #creates an empty tuple
courses_tuple = tuple() #also creates an empty tuple
courses_tuple = ("History", "Math", "Physics", "CompSci") #creates a tuple of strings
#tuples can do just about anything lists can do, as long as it doesnt change anything about the tuple, i.e: accessing, looping, finding

## Sets - like a list and tuple, but it will ignore duplicates

# creating sets - uses {} instead of [] or ()
courses_set = set() #ONLY WAY TO CREATE AN EMPTY SET, JUST {} CREATES A DICTIONARY
courses_set = {"History", "Math", "Physics", "CompSci"} #creates a set of strings; HOWEVER, each time you print it, it will appear in a different order. IF there is a duplicate in a set, it will ignore it, printing only 1 instance of an item

# .intersection(set2) - returns a set with the values in the set1 calling the method that are also in the set2 passed as an argument
art_courses = {"History", "Math", "Art", "Design"}
courses_set.intersection(art_courses) #returns the set: {"History", "Math"} - in any order

# .difference(set2) - returns a set with the values in the set1 calling the method that are NOT in the set2 passed as an argument
courses_set.difference(art_courses) #returns the set: {"Physics", "CompSci"} - in any order

# .union(set2) - returns a set with the values in both the set1 calling the method and the set2 passed as an argument
courses_set.union(art_courses) #returns the set: {"History", "Math", "Art", "Design", "Physics", "CompSci"} - in any order

### Dictionaries - same thing as hashmaps, key-value pairs

## creating a dictionary
student = {} # creates an empty dictionary
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]} # each comma separates a key-value pair.

## accessing a dictionary

#print(student) #prints out all of the keys and values
student["name"] #returns "John" - uses key to access value. If key does not exist you will get a KeyError

# .get(key) - returns value at key, if key does not exist it will return NONE
student.get("name") #returns "John"

# .get(key, missingMessage) - returns value at key, if key does not exist it will return "missingMessage"
student.get("phone", "Not Found") #returns "Not Found"

## modifying dictionaries

# setting a value to a new key in dictionary
student["phone"] = "555-5555" #adds "phone": "555-5555" to student dictionary

# .update(dict) - adds or modifies dictionary calling method using the keys and values from the dictionary passed in the argument
student.update({"name": "Jane", "age": 26, "phone": "555-5555"}) #changes name to Jane, age to 26, and adds "phone": "555-5555" (assuming phone was not already there), rest of key-value pairs stay the same

# del dictionary[key] - deletes key-value pair form dictionary
del student["age"] #deletes age key-value pair from dictionary

# .pop(key) - deletes key-value pair from dictionary calling the method and returns the value
phone = student.pop("phone") #deletes phone key-value pair from dictionary and returns value in age variable

## looping through keys and values in a dictionary

# len(dict) - returns number of keys or key-value pairs in dictionary
len(student) #returns 3

# .keys() - returns the keys in dictionary calling the method
student.keys() #returns dict_keys{["name", "age", "courses"]}

# .values() - returns the values in dictionary calling the method
student.values() #returns dict_values{["John", 25, ["Math", "CompSci"]]}

# .items() - returns the key-value pairs in dictionary calling the method
student.items() #returns dict_items([("name", "John"), ("age", 25), ("courses", ["Math", "CompSci"])])

# for loops
    #can use any name for "key" to return the keys in "student" dictionary
for key in student:
    #print(key) #returns the keys in dictionary students
    break

#  use .items() to loop thru the key-value pairs

for key, value in student.items():
    #print(key, value) #returns the key-pair values in dictionary students
    break

### CONDITIONALS

## if, elif, and else statements
language = "Python"
if language == "Python":
    print("Conditional was True")
elif language == "Java":
    print("Language is Java")
else:
    print("No match")

## and, or, not, is operators

# and - both sides of the operator have to be true to pass
logged_in = False
internet = True

if logged_in and internet:
    print("You can log-in!")
else:
    print("You cannot log-in.")

# or - only one of the sides of the operator has to be true to pass
if logged_in or internet:
    print("You can almost log-in!")
else:
    print("You absolutely cannot log-in.")

# not - switches booleans (T to F, F to T)
if not logged_in:
    print("Logged out")
else:
    print("Logged in!")

# is - checks object identity, returns bool, same as (id(a) == id(b))

a = [1,2,3]
b = [1,2,3]
(a is b) #returns false, they have different memory addresses
b = a
(a is b) #returns true, they have the same memory address

# False values - if a variable or object is set to any of these values, it will always evalute to false in a conditional
False
None
0
(), {}, [], "", ''
# THIS IS EXTREMELY USEFUL FOR TESTING IF AN OBJECT IS EMPTY, IF A STRING OR A LIST OR WHATEVER IS EMPTY IT WILL EVALUATE TO FALSE IN A CONDITIONAL WITH JUST THE VARIABLE
condition = ()
if condition:
    print("This is not an empty tuple")
else:
    print("This is an empty tuple!!")

### LOOPS & ITERATIONS