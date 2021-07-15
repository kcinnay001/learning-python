# tutorial link: https://www.youtube.com/watch?v=rfscVS0vtbw&t=15333s
# tutorial time: 34:00


from math import *
from chef import Chef
from chineseChef import ChineseChef
from student import Student # from the student file import student class
from os import error
import useful_tools # import this from the file

print("Hello World") # allows you to write comments


## Making a triangle shape -> print the code comment out to the console in order
##------------------------------------------------------------------------------

print("     /| ")
print("    / | ")
print("   /  | ")
print("  /   | ")
print(" /    | ")
print("/_____| ")

## Using variables and datatypes -> container to store data values
##----------------------------------------------------------------

character_name = "Yannick"
character_age = "20"

print(character_name + " " + character_age)


## Different Data Types
##---------------------

# string - name = "",
# numbers - myNumber = 25 or 50.2
# Boolean - isMale = True


## Working with strings -> everything you can do with strings
##-----------------------------------------------------------

phrase = "Yannick"
print( phrase + "\nis Learning") # adding a new line and concatenation
print("Yannick \"Learning\"") # adding quotation marks
print(phrase.lower()) # string methods
print(phrase.lower().isupper()) # checks to see if it's uppercase
print(len(phrase)) # shows the length of the string
print(phrase[3]) # getting individual characters in a string -> should print Y
print(phrase.index("Y")) # index function -> show the index of that letter in the string
print(phrase.replace("Yan","Man")) # Replace a string with another alternative

# Google search will show you all the string function

## Working with Numbers
##---------------------

print(2) # prints 2 into the console
print(2.1) # print decimal
print(-2.1) # prints negative
print(3 * 4) # can perform mathmatical equations
print(3 * (3 + 5)) # can preform bidmas
print(10 % 3) # returns the remainder -> mainly shows if the remainder is in the function
my_num = -5; # Storing inside a varibale
print(my_num)
print(str(my_num) + 'my favourite number') # converting number to a string
print(abs(my_num)) # absolute value -> will print 5
print(pow(3,2)) # raises it to the power of the second parameter
print(max(4,6)) # returns which number is higher
print(min(4,6)) # returns which number is lower
print(round(3.2)) # returns the number rounded

# You have to install the module when you do this next section math
# |
# |
# V
print(floor(3.7)) # grabs the lowest number in the number
print(ceil(3.7)) # rounds the number up no matter what
print(sqrt(36)) # returns the square root of the passed number

## Getting input from a user
##--------------------------
# name = input("Enter Your Name: ") # tells python you want to get input from a user -> then string passed through is the prompt -> stores value in variable
# print('hello ' + name + '!'); # prints the value the user entered
# age = input("Enter age: ") # by defualt converts number to a string
# print("You are "+ age +" years old")


## Building a calculator
##----------------------
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + int(num2) # converts the string to a whole number -> can't have decimals
# result = float(num1) + float(num2) # converts the string to a whole number and use decimals -> allows you to enter any number you want
# print(result)

## Building a mad lib game
##------------------------
# taking inputs
# color = input("Enter a color: ")
# pluralnoun = input("Enter a plural noun: ")
# something = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(pluralnoun+" are blue")
# print("I love " + something)


## Working with lists
##-------------------

friends = ["Josh","Tom","Adam","Sam","Sam","Nathan","Lewi"] # creating a list -> allows you to store mutiple values inside one variable
                                                      # Anything can be stores in the variable
print(friends) # prints all the friends in the list
print(friends[2]) # specific friend
print(friends[1:]) # grabs the index at 1 and everything after
print(friends[1:3]) # specify a range to grab from

## List functions
##---------------
lucky_number = [1,2,3,4]
# friends.extend(lucky_number) # adding two list together
friends.append("Lewis") # adding an item at the end of the list
friends.insert(1, "Declan") # inserts the item at an index
friends.remove("Adam") # removes the item in that list specified
# friends.clear() # removes everthing in the list
friends.pop() # gets rid of the last element in the list
friends.index("Sam") # shows the index of the value in the list -> values not found will throw an error
friends.count("Sam") # how many times the value shows up in the list
friends.sort() # sorts the list in ascending order -> letter (alphabetical order) -> numbers(ascending order)
lucky_number.reverse() # changing the order of the lists
friends2 = friends.copy() # duplicates the original list in a different variable
print(friends)

## Tuples -> can store multiple pieces of information
##---------------------------------------------------

coordinates = (4,5) # creating a tuple -> they are immuteable -> can't be changed or modified
print(coordinates[0]) # print out the tuple
# difference between tuple and list -> you can't manipulate the late -> used for data that is never going to change
other_coordinates = [(6,7),(8,9)] # creating a list of tuples

## functions -> collection of code that performs a task
##-----------------------------------------------------

# allows you to organise your code

# creating a function that says hi
def sayHi(): # all the code that comes after the line will be in the function
    # code needs to be indented to be counted in the function
    print("Hello User")

sayHi() # calling the function -> prints the function in order

def sayBye(name): # passing parameters -> you can have as many parameters as you want
    print("Bye " + name)

sayBye("Bob")

## Return Statement
##-----------------
# allows python to return information from a function
def cubeNum(num1): # function to return a cube number
    return floor(pow(num1,3)) # no code will be executed after the return is called -> breaks out of the function

result = cubeNum(5) # stores the value stored in the function
print(result) # printing the value stored in the variable

## IF Statements
##--------------
# help algorithm make condition
is_male = True # creating a boolean variable
is_tall = True

if is_male: # anything below this with an indent is executable code
    print("you are a male")
else: # an otherwise condition
    print("You are not a male")

if is_male or is_tall: # will get executed when one the conditions is true
    print("I am tall and male")
else:
    print("You are neither nor tall")

if is_male and is_tall: # will get executed when both are true
    print("You are tall and a male")
elif is_male and not(is_tall): # the not will reverse the value of the passed boolean same as ! in javascript
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are either not tall or not a male")

## Comparison Operators -> can compare numbers and can compare strings
##--------------------------------------------------------------------

def makeNum(num1,num2,num3): # will print out the biggest num
    if num1 >= num2 and num1 >= num3: # comparing numbers
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(makeNum(3,4,5))

# >= ,== ,!== ,<= ,> ,<


## Building a better calculator
##-----------------------------

# num1 = float(input("Enter first number"))
# num2 = float(input("Enter second number"))
# op = input("Enter operater(-,+,/,*): ")

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("invalid number")


## Dictionaires
##-------------

# allows you to store information in key value pairs

monthConversions = { # creating a dictionaires -> like an object
    "Jan":"January", # all the keys have to be unique
    "Feb":"February",
    "Mar":"March"
}

print(monthConversions["Jan"]) # accessing the key
print(monthConversions.get("Mar")) # another accesing method
print(monthConversions.get("luv")) # accessing method that dosent exist
print(monthConversions.get("luv","not a valid key")) # accessing method that dosent exist -> return a default value


## While loop
##-----------

# allows you to loop through code multiple times

i = 1

while i<=10: #keep looping through the code if the condition is true
    print(i)
    i += 1

print("done with loop")

## For Loops
##----------

# allows you to loop through a collection of items

for letter in "Yannick": # looping through all the letter in the string
    print(letter)

for f in friends: # looping through an array
    print(f)

for index in range(10): # looping through a range -> you can do range(3,10)
    print(index)

for y in range(len(friends)): # looping through the normal way
    print(friends[y])


## Exponent function
##------------------

print(2**3) # 2 to the power of 3

def raiseToPower(baseNum,powNum):
    result = 1
    for g in range(powNum):
        result = result * baseNum
    return result

print(raiseToPower(4,10)) # How the to pow function works

## 2d lists
##---------

numberGrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(numberGrid[0][0]) ## getting the element in the array

## Nested for loop
##----------------

for row in numberGrid:
    for col in row:
        print(col)


# if letter in "AEIOUaeiou" # checking if value contains a letter


## Try/Expect
##-----------

# def numberFunction():
#     number = int(input("Enter a Number: "))
#     print(number)

# try:
#     numberFunction()
# except ValueError as err: # this catches any error use the error specific to what you want
#     print("Invalid input")


## Reading external files
##-----------------------

#open file in python
employee_file = open(
 "employees.txt"
,"r" # read # w - write -> override the entire file # a - append # r+ - read and write
) # path to the file
# after open you want to close

print(employee_file.readable()) # shows if the file can be read from
# print(employee_file.read()) # reads all the info in the file
# print(employee_file.readline()) # reads a line in the file
# print(employee_file.readlines()) # puts each line in an array
for employee in employee_file.readlines():
    print(employee)

employee_file.close() # closing the file -> must do at the end


## Writing and appending to file
##------------------------------

employee_file = open("employees.txt","a")
# employee_file = open("employees1.txt","w") #adding a new file
# employee_file1 = open("employees1.html","w") # creating a html file
# employee_file1.write("<p>All html</p>") # writing to a html file

# employee_file.write("\nToby - human resources") # adding to the end of the file

employee_file.close()


## Module and pips
##----------------

# module - python file you can import into another file -> any external python file

# import at top of the file ^^

print(useful_tools.rollDice(10))

# python module index  -> shows all the python modules -> like npm for node
# built in modules -> built into python
# external modules -> installed on the same folder that came with the computer

# installing third party modules -> python-docx -> pip install python-docx
# step #
# |
# |
# v
# open command
# pip --version -> shows you have pip install
# pip install python-docx -> installs the document


## classes and objects
##--------------------

# represent data that is not representable

# Modelling a student -> creating a student

# you have to import the student class from the student folder  ^^

student1 = Student("Jim","Business",3.1,False) # creating a student -> basically creates a student datatype

print(student1.name) # prints jim


## Object functions
##-----------------

# function you can use inside a class
# look inside the student class

print(student1.on_honor_roll())


## Inheritance
##------------

myChef = Chef()
myChineseChef = ChineseChef()
myChef.make_chicken()
myChineseChef.make_fried_rice()


## Python Interpreter 
##-------------------

# allows you to test python 

# open command prompt -> cmd 