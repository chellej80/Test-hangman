# import random
import time
from words import select_word
from hang_man_pics import hangman_pic

ALPHABETS = ('abcdefghijklmnopqrstuvwxyz')
# Statements welcoming the user and asking for them to input their name
def print_with_sleep(msg, sleep_interval):
    print(msg)
    time.sleep(sleep_interval)

def take_username_input():
    name = input("Enter your name: \n")
    if name.isalpha():
        return name.capitalize()
    else:
        print('Please enter your name using letter only: \n')
        return take_username_input()
# Statements welcoming the user and asking for them to input their name
def show_greeting_and_take_username():
    print("-------------------------------------------")
    print("Welcome to Horsey Hangman")
    print("-------------------------------------------")
    name = take_username_input()
    print("-------------------------------------------")
    # Use a decision making process to accept only alphabets as name
    print_with_sleep("Hello" + " " + name + " " +  "let's start playing Hangman!", 1)
    print_with_sleep("The objective of the game is to guess the secret word one letter at a time", 1)
    print_with_sleep("Don't forget to press 'enter key' after each guess.", 2)
    print_with_sleep("Let the fun begin!", 1)

def play_again():
    
    """ This function asks user/player if he/she wishes to replay"""
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()

    # Create a decision making process
    if response == 'y':
        run_game()
    else:
        print("Hope you enjoyed the game !. See you next time :)")

# Define function to run the gamey
def run_game():
    # call the greeting function to get the game running
    # greeting()
    # show_greeting_and_take_username()
    
    # Define a variable alpahabet
    # alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
    # Set guess word to get_word function for a random word to be generated
    word = select_word()
    
    # Initiate an empty list for guessed letter
    guessed_letters = []
    
    # Initiate a counter for number of tries by the user
    total_attempt_counter = 6
    
    # Set inital guess to false
    sucessfully_guessed = False

    wrong_guess = 0
     
    # Print an empty line
    print()

    # Initate a while loop and create decisions
    # Also a create decisions for if user inputs a wrong entry
    # Deduct attempts each user fails to guess incorrectly
    while sucessfully_guessed is not True and total_attempt_counter > 0:
        print('You have ' + str(total_attempt_counter) + ' attempts')
        guessed_letter = input('Guess a letter: \n').lower()
        #user inputs a letter
        if len(guessed_letter) == 1:
            if guessed_letter not in ALPHABETS:
                print('You are yet to enter a letter. Check your entry, make sure you enter an alphabet not a number')
            elif guessed_letter in guessed_letters:
                print('You have already guessed that letter before.Try again!')
            elif guessed_letter not in word:
                print('Sorry, that letter is not part of the word')
                guessed_letters.append(guessed_letter)
                total_attempt_counter -=1
                wrong_guess +=1
                hangman_pic(wrong_guess)
            elif guessed_letter in word:
                print('Super that letter is in the word')
                guessed_letters.append(guessed_letter)
                # nattempt_counter -=1
                hangman_pic(wrong_guess)
        else:
            print('Please enter only one Letter per try')
            total_attempt_counter -=1  
        # print letter or dash under hangman pic
        result = ''
        if sucessfully_guessed is not True:
            for letter in word:
                if letter in guessed_letters:
                    result += letter
                else:
                    result += '_'
            print(result.capitalize())
           

        if result == word:
            print()
            sucessfully_guessed = True
            print("Well Done you guessed the right word :)")
            print("-------------------------------------------")
            
        elif total_attempt_counter == 0:
            print()
            print("-------------------------------------------")
            print("Opps! You ran out of guesses, Hard Luck !!")
            print("The correct word was: ", word.capitalize())
            print("-------------------------------------------")

    #Initiate play_again function if user wishes to continue
    play_again()

def start_game():
    show_greeting_and_take_username()
    run_game()

#Full program run
start_game()
