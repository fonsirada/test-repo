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

## Escape sequnces

#\n #new line
#\t #tab
#\\ #backslash (\)
#\' #single quote (')
#\" #double quote (")

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
    #print("Conditional was True")
    pass
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
    #print("You cannot log-in.")
    pass

# or - only one of the sides of the operator has to be true to pass
if logged_in or internet:
    #print("You can almost log-in!")
    pass
else:
    print("You absolutely cannot log-in.")

# not - switches booleans (T to F, F to T)
if not logged_in:
    #print("Logged out")
    pass
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
    #print("This is an empty tuple!!")
    pass

### LOOPS & ITERATIONS

nums = [1,2,3,4,5]

# break keyword - breaks out of for loop when called
for num in nums:
    if num == 3:
        #print('Found!')
        break
    #print(num) #returns 1 2 "Found!" (break)

# continue keyword - skips to next iteration when called
for num in nums:
    if num == 3:
        #print("Found!")
        continue
    #print(num) # returns 1 2 "Found!" (continue) 4 5

## loops within loops
for num in nums:
    for letter in "abc":
        #print(num, letter) #returns 1 a, 1 b 1 c 2 a 2 b 2 c ...
        pass

# for loops in range - runs for set nuumber of iterations (or a break)
        #10 iterations
for i in range(10):
    #print(i)
    pass
            #starts at 1 goes up to 11 (exclusive)
for i in range(1, 11):
    #print(i)
    pass

# while loops - runs until condition is no longer met (or a break)
x = 0
while x < 10:
    #print(x)
    x += 1

# common infinite loop that runs until a break
x = 0
while True:
    if x == 5:
        break
    #print(x)
    x += 1

## Functions - instructions packaged together that perform a specific task

# constructing a function
def hello_func():
    pass #allows the function to pass without leaving it blank

#print(hello_func) # returns the memmory address

# parameters
def func(greeting):
    return '{} Function.'.format(greeting)
func("Hi") #returns 'Hi Function.' - need to call print

def func2(greeting, name="Stranger"):
    return "{}, {}".format(greeting, name)
func2("Hi") #returns 'Hi, Stranger" - uses default from parameter, if no name is passed as an argument
func2("Hi", "Alfonso") #returns 'Hi, Alfonso'
func2("Hi", name="Alfonso") #also returns 'Hi, Alfonso'

# functions with unknown amo. of arguments, positional args and positional keyword args
                #arguments, keyword arguments i.e: name = "Stranger"
def student_info(*args, **kwargs):
    """This is a docustring that explains what a function does"""
    #print(args) # returns a tuple holding the positional arguments
    #print(kwargs) # returns a dictionary holding the keyword arguments and their values
    pass

student_info("Math", "Art", name="John", age=22)

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(courses, info) #returns both courses and info in positional arguments tuple

student_info(*courses, **info) #returns the same thing as student_info("Math", "Art", name="John", age=22), with courses in tuple and info in dictionary

### IMPORTING MODULES & STANDARD LIBRARY
import os
os.getcwd() #returns current working directory

##### PYTHON OOP

### Classes - logically group data and functions in a way that is easy to reuse and build upon

# attributes - variables within an object/class

# methods - functions that are associated with an object/class

# constructing a class
class Employee:
    pass

# These are each their own unique instances of the Employee object/class, they have different memory addresses
emp_1 = Employee() 
emp_2 = Employee()

#print(emp_1) #returns memory address 
#print(emp_2) #returns memory address

#instance variables contain data that is unique to each instance

emp_1.first = "Alfonso"
emp_1.last = "Rada"
emp_1.email = "arada@hamilton.edu"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 60000

#instead of having to write out all of this code for each employee, we can just use functions within our class, methods.

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    #think of this as the constructor
            #the instance is always the first argument received (self)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        #can also alter class variables across all instances within the class itself
        Employee.num_of_emps += 1
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
                #each instance can access class variables, and also have a unique value for it
        self.pay = int(self.pay * self.raise_amount)

    @classmethod #cls is class, like self but for the whole class, not just 1 instance
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod #does not pass self or cls as an argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

#now you can just pass the data as arguments and set up the instance variables much more efficiently
emp_1 = Employee("Alfonso", "Rada", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_1.email #returns the email of emp_1 instance
emp_2.email #returns the email of emp_2 instance

emp_1.fullname() #calls fullname() method of Employee object and returns fullname of instance emp_1

#Employee.fullname() #this will return an error because an instance is not given, leaving the argument 'self' without a variable.
Employee.fullname(emp_1) #this will work because now self has a value, emp_1
emp_1.fullname() #this will work because emp_1 is an instance and is calling the method

#Each instance can access class variables, and also have a unique value for it
#Employee is the class, so the default value of raise_amount for all Employee object instances is 1.04
Employee.raise_amount #returns 1.04
emp_1.raise_amount #return 1.04
#however, you can set instances to have unique values for class variables (adding the attribute to the instance)
emp_2.raise_amount = 1.05
emp_2.raise_amount #returns 1.05

# .__dict__ - returns dictionary containing the attributes in object calling it
emp_2.__dict__ #returns a dictionary of the attributes in emp_2: {'first': 'Test', 'last': 'User', 'pay': 60000, 'email': 'Test.User@company.com', 'raise_amount': 1.05}

## Class methods - makes changes across the entire class, not just an instance, takes in the class as an argument rather than self

Employee.set_raise_amt(1.07) #changes the raise_amount class variable for the Employee class/object
emp_1.raise_amount #returns 1.07
Employee.raise_amount #returns 1.07 (default class variable)
emp_2.raise_amount #stays at 1.05 because raise_amount was not the default, it was user set to 1.05

emp_str_1 = "John-Doe-70000"
new_emp = Employee.from_string(emp_str_1) #creates a new instance of Employee object/class using from_string classmethod, behaves kind of like a constructor

## Static methods - do not pass the instance or the class as arguments, unlike regular methods and class methods, they behave just like regular functions. A giveaway that a method should be static is if an instance or a class is not accessed at all in the function

### Inheritance & Subclasses

# declares that Developer is a subclass of Employee class (inherits Employee's attributes and methods)
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #same as Employee.__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())
            
dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "Developer", 60000, "Java")
dev_1.email #works the same, returns Corey.Schafer@company.com
dev_2.prog_lang #returns "Java"

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# all methods that are unique only to Manager objects
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

# help function
#help(Developer) # outputs the methods and attributes inheritied from superclass as well as method resolution order

# method resolution order - order that instance looks for methods
# 1. Developer (subclass) 2. Employee (superclass)

# isinstance(object, class) - returns bool that declares whether object is an instance of class
isinstance(mgr_1, Manager) #returns true

# issubclass(class1, class2) - returns bool that declares whether class1 is a subclass of class2
issubclass(Manager, Employee) #returns true
issubclass(Manager, Developer) #returns false

## Special (Magic/Dunder) Methods - operator overloading

# methods surrounded by double underscores are Dunder methods (__) i.e: __init__

# These are 2 MUST HAVE dunder methods, __repr__ and __str__
# __repr__(self) method - outputs when print(inst) is called, also a fall back for if __str__ doesn't exist.
emp_1.__repr__()
repr(emp_1)

# __str__(self) method - outputs when print(inst) is called, has higher priority than __repr__.
emp_1.__str__()
str(emp_1)
#print(emp_1) # returns __str__ output, not __repr__ since __str__ exists and has higher priority

# __add__(self, other) - operator overload function for adding Employee objects,
emp_1 + emp_2 #returns the pay of emp_1 added to the pay of emp_2

# __len__(self) - operator overload function for finding the length of an Employee object
len(emp_1) #returns number of characters in an employees name

## Property Decorators - Getters, Setters, and Deleters

# @property decorator - allows a method to be called like an attribute (Getter)

class Test_Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def __str__(self):
        return "{}, {}".format(self.fullname, self.email)
    
test_emp = Test_Employee("Jesus", "Rada")
test_emp.email #returns output of email method since it has @property above it, Jesus.Rada@company.com

# @'method name'.setter decorator - allows a method to be called like an attribute and set to a variable (Setter) - 'method name' method must have property decorator above it
test_emp.fullname = "Gleyber Torres" #sets Gleyber Torres to test_emp's fullname, even though it's a method and not an attribute
test_emp.email #returns output of email method, which would be Gleyber.Torres@company.com

# @'method name'.deleter decorator - runs when del instance.'method name' is called - 'method name' method must have property decortor above it

del test_emp.fullname #returns fullname.deleter method, which sets self.first and self.last to None
