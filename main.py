import os
import random

def menu():
    print("Please choose form the list of excersizes below:")
    print("Exercise #1 - usinput ")
    print("Exercise #2 - reverse")
    print("Exercise #3 - counter")
    print("Exercise #4 - replace")
    print("Exercise #5 - menu")
    print("Exercise #6 - analysis")
    
    
    
    #this is the test of the menu
    choice = int(input(":>"))
    
    #write the condition to call each function
    if choice == 1: #call excersize 1
        print("Calling excersize 1... ")
        usinput()
    elif choice  == 2: #call excersize 2
        print("Calling excersize 2... ")
        reverse() 
    elif choice  ==3 : #call excersize 3
        print("Calling excersize 3... ")
        counter()
     
    elif choice  == 4: #call excersize 4
        print("Calling excersize 4... ")
        replace()
     
    elif choice  == 5: #call excersize 5
        print("Calling excersize 5... ")
        menu()
     
    elif choice  == 6: #call excersize 6
        print("Calling excersize 6... ")
        analysis()
     
    else:
        print("Thank you for using chapter 8 menu")
    
    choice = 0
    
    
def usinput():
    #program 1
    #ask the user for a string
    #check if the strig is at least five letters and only letters
    global user_input
    count = 0
    user_input = input(f"Enter a rale word that is five letters and only letters: ")
    if user_input.isalpha():
        for letters in user_input:
            count = (count + 1)
        if count > 4:
            m = 0
    else:
        print('the user input is not exsepted')
    menu()

def reverse():
    w = 0
#revers the string and return it
    moo = 1
def counter():
    global user_input
    constints = 0
    vawles = 0
    bill = 0
    for letter in user_input:
        timmy = user_input[bill]
        bill = (bill + 1)
        if timmy == 'a' or timmy == 'e' or timmy == 'i' or timmy == 'o' or timmy == 'u':
          vawles = vawles + 1
        elif timmy == 'A' or timmy == 'E' or timmy == 'I' or timmy == 'O' or timmy == 'U':
          vawles = vawles + 1
        else:
          constints = constints + 1
    return vawles, constints

def replace(user_input):
#replace spicific letters with another letter
  timmy = input('enter the letter you want to replace')
  bimmy = input('enter the letter to replace it with')
  user_input.replase(timmy, bimmy)
  return user_input

def analysis():
    letter = 0
    1 == 'm'
    for letters in user_input:
        letter = (letter + 1)
        letternow = letters
        letterw = letter
        letterw = letters
        print(letter)
        print(letterw)
        
#retuns if string is a palindrone
#retuns total letters
#returns total constins (call counter to make it faster)
#returns total vawls (call counter to make it faster)
