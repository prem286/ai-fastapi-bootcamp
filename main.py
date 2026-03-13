#-----Rock, Paper, Scissors Intro Project-----

# import random

#print("Hello World !!!!")



# def get_choice():
#     #player_choice = "rock" #local variable
#     player_choice = input("Enter a choice ")
#     options = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(options)
#     #computer_choice = "paper" #loca variable
#     choices = {"player": player_choice, "computer": computer_choice}
#     #return computer_choice
#     return choices



# def greeting():
    
#     return "Hi"

#calling function greeting()
# response = greeting()
# print(response)


#calling function get_choice()
# choices = get_choice()
# print(choices)


#Dictionaries keywoard 'dict' to store the key value pairs
#dict = {"name" : "Pratosh", "color": "blue"}


#If Statements
# a = 3
# b = 5

# if a < b:
#     print("Yes")


#Function Arguments
# def check_win(player, computer):
#     #print("You chose " +player + ", computer chose " +computer) # Concatenating Strings 
#     print(f"You chose {player}, computer chose {computer}") #f-strings
#     if player == computer:
#        return "It's a tie!"
    
#calling function
# response = check_win("rock", "paper")
# print(response)

#--------------------------Fundamentals of Python------------------------


#In Python, data types are automatically detected, so developers do not need to explicitly specify types such as string, int, double, or float
#Data type String
name = "Pratosh"
print("Name is : ",name)

print("What is data type: ",type(name))

print("name data type is str ?:-->  ",type(name) == str)

print("Is instance name is str?:--> ",isinstance(name, str))
print("----------------------------------")

#Data type int 
age =34
print("Age is : " ,age)
print("What is Data type:--> ", type(age))
print("Is instance  is int?:--> ",isinstance(age, int))
print("----------------------------------")

#In Python, data type conversion can be done using class constructors such as int(), float(), str(), etc. So the concept is called Type Casting (Type Conversion) in Python.
age =float(34)
print("Is instace is  float: ", isinstance(age, float))

a = "5" # String 
b = int(a) # Convert to integer
print(b)

x = 6
y = float(x)
print(y)



#-------------Operator------------------------

#Operators are symbols used to perform operations on variables and values.

age =8
age += 8
print(age) # age = age + 8

age =8
age *= 8
print(age) # age = age * 8


a= 10
b=5
print(a> b and b < 10) #True
print(a < 5 or b < 10) # True
print(not(a > 5)) # False
print("----------------------------------------")

#----------------------Strings------------------

print("Convert all letter in upper case: ","Pratosh".upper()) # O/P- PRATOSH
print("Convert all letter in lower case: ", "Pratosh".lower()) # O/P- pratosh
print("Convert all letter in camel case: ", "pratosH kUmAr".title()) # O/P- Pratosh Kumar
print("pratosh".islower()) # O/P- True
print("pratosh".isupper()) # O/P- False

First_Name= "Pratosh"
print("ra" in First_Name) # Value exists in sequence/string and it will return True/False


#String Characters & Slicing


name = "Pratosh"
print(name[1]) # It will return the index value from string, indexing starting from 0
print(name[-1]) # O/P- h
print(name[1:4]) # return the the value from string take start index include and end index exclude 
print(name[0:2]) # O/P- Pr
print(name[:4]) # O/P- Prat
print(name[2:]) # O/P - atosh
print(name[:]) # O/P- Pratosh

print(name[::2]) # O/P- Paoh, every 2nd character
print(name[::-1]) # O/P- hsotarP,  reverse string)

print(name[-3:]) #O/P- osh, Last characters
print(name[:-2]) # O/P- Prato
print("----------------------------------")

# ============================================================
# BOOLEANS
# ============================================================

# Boolean data type represents one of two values:
# True or False

a = True
b = False

# Booleans are often used in conditions

print(10 > 5) # O/P - True
print(5 > 10) # O/P - False

ingreidents_purchased = True
meal_cooked = False

ready_to_server = any([ingreidents_purchased, meal_cooked])
print(ready_to_server) # O/P- True, Returns True if at least one element in the iterable is True

ready_to_server = all([ingreidents_purchased, meal_cooked])
print(ready_to_server) # O/P- False, Returns True if all elements in the iterable are True

bool(1)
bool(0)







