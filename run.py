import random
import time

# Function to hold the Hangman design, passing in wrong as an argument
def hangman_pic(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


# Statements welcoming the user and asking for them to input their name
def greeting():
    print("-------------------------------------------")
    print("Welcome to Horsey Hangman")
    print("-------------------------------------------")
    name = input("Enter your name: \n")
    print("-------------------------------------------")
    # Use a decision making process to accept only alphabets as name
    if name.isalpha() == True:
        print("Hello", name.capitalize(), "let's start playing Hangman!")
        time.sleep(1)
        print("The objective of the game is to guess the secret word one letter at a time")
        time.sleep(1)
        print("Don't forget to press 'enter key' after each guess.")
        time.sleep(2)
        print("Let the fun begin!")
        time.sleep(1)
                  
    else:
        print('Please enter your name using letter only: ')
        name = input("Enter your name: \n")
        print("Hello", name.capitalize(), "let's start playing Hangman!")
        time.sleep(1)
        print("The objective of the game is to guess")
        time.sleep(1)
        print("Don't forget to press 'enter key' after each guess.")
        time.sleep(2)
        print("Let the fun begin!")
        time.sleep(1)


def play_again():
    
    """ This function asks user/player if he/she wishes to replay"""
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()

    # Create a decision making process
    if response == 'y':
        run_game()
    else:
        print("Hope you enjoyed the game !. See you next time :)")

# Define a function for generating random words for the user to guess.
def select_word():
    """ This function generates the word the user will attempt guessing"""
    words = ["Horse", "Pony", "Saddle", "Bridle", "Girth", "Equine"]
    return random.choice(words).lower()

# Define function to run the gamey
def run_game():
    # call the greeting function to get the game running
    greeting()
    
    # Define a variable alpahabet
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
    # Set guess word to get_word function for a random word to be generated
    word = select_word()
    
    # Initiate an empty list for guessed letter
    guessed_letters = []
    
    # Initiate a counter for number of tries by the user
    attempt_counter = 6
    
    # Set inital guess to false
    guessed = False
     
    # Print an empty line
    print()

    # Initate a while loop and create decisions
    # Also a create decisions for if user inputs a wrong entry
    # Deduct attempts each user fails to guess incorrectly
    while guessed == False and attempt_counter > 0:
        print('You have ' + str(attempt_counter) + ' attempts')
        guess = input('Guess a letter: \n').lower()
        #user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You are yet to enter a letter. Check your entry, make sure you enter an alphabet not a number')
            elif guess in guessed_letters:
                print('You have already guessed that letter before.Try again!')
            elif guess not in word:
                print('Sorry, that letter is not part of the word')
                guessed_letters.append(guess)
                attempt_counter -=1
                hangman_pic(attempt_counter)
            elif guess in word:
                print('Super that letter is in the word')
                guessed_letters.append(guess)
                # nattempt_counter -=1
                hangman_pic(attempt_counter)
        else:
            print('Please enter only one Letter per try')
            attempt_counter -=1  
        # print letter or dash under hangman pic
        result = ''
        if guessed == False:
            for letter in word:
                if letter in guessed_letters:
                    result += letter
                else:
                    result += '_'
            print(result)
           

        if result == word:
            print()
            guessed = True
            print("Well Done you guessed the right word :)")
            print("-------------------------------------------")
            
        elif attempt_counter == 0:
            print()
            print("-------------------------------------------")
            print("Opps! You ran out of guesses, Hard Luck !!")
            print("The correct word was: ", word)
            print("-------------------------------------------")

    #Initiate play_again function if user wishes to continue
    play_again()

#Full program run
run_game()