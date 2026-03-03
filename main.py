import random

#print("Hello World !!!!")



def get_choice():
    #player_choice = "rock" #local variable
    player_choice = input("Enter a choice ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    #computer_choice = "paper" #loca variable
    choices = {"player": player_choice, "computer": computer_choice}
    #return computer_choice
    return choices



def greeting():
    
    return "Hi"

#calling function greeting()
response = greeting()
print(response)


#calling function get_choice()
choices = get_choice()
print(choices)


#Dictionaries keywoard 'dict' to store the key value pairs
dict = {"name" : "Pratosh", "color": "blue"}