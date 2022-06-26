import random
import time
import os
#imports the libaries used

def guess(x): #Defines the value to make the code a bit cleaner with def

    test = random.randint(1, x) #Defines the value from number minimum to maximum
    guess = 0 
    while guess != test: #A loop used to make sure the loop ends when you guess the correct number

        guess = int(input(f"Guess a number between 1 and {x}: ")) # Takes our user input of the value

        if guess > x: #Defines the if statment if guess is smaller than our defined value (x)
            print("Aim lower") #Prints the clue 
            time.sleep(2) #Delays the console clearing for 2 seconds to give the user enough time to read
            os.system("cls") #Clears the console

        elif guess < x: #Defines the elif statment if guess is greater than our defined value (x)
            print("Aim higher") #Prints the clue
            time.sleep(2) #Delays the console clearing for 2 seconds to give the user enough time to read
            os.system("cls") #Clears the console

    print(f"You guessed the correct number {test}") #Tells the user that they guessed the correct number

guess(69) #Selects the top number you want to be able to guess
