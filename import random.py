import random
import time

# Function to hold the Hangman design, passing in wrong as an argument

# Should be in constants file
HANGMAN_STATES_BY_LIVES_LEFT = {
    0: "\n+---+    |        |   ",
    1: "\n+---+    |        |   ",
    2: "\n+---+    |        |   ",
    3: "\n+---+    |        |   ",
    4: "\n+---+    |        |   ",
    5: "\n+---+    |        |   ",
    6: "\n+---+    |        |   ",
}

ALPHABETS = ('abcdefghijklmnopqrstuvwxyz')

def hangman_pic(wrong):
    lives_left = 6 - wrong 
    print(HANGMAN_STATES_BY_LIVES_LEFT[lives_left])

def print_with_sleep(msg, sleep_interval):
    print(msg)
    time.sleep(sleep_interval)

def take_username_input():
    name = input("Enter your name: \n")
    if name.isalpha():
        return name
    else:
        print('Please enter your name using letter only: ')
        return take_username_input()


# Statements welcoming the user and asking for them to input their name
def show_greeting_and_take_username():
    print("-------------------------------------------")
    print("Welcome to Horsey Hangman")
    print("-------------------------------------------")
    name = take_username_input()
    print("-------------------------------------------")
    # Use a decision making process to accept only alphabets as name
    print_with_sleep("Hello" + name.capitalize() +  "let's start playing Hangman!", 1)
    print_with_sleep("The objective of the game is to guess the secret word one letter at a time", 1)
    print_with_sleep("Don't forget to press 'enter key' after each guess.", 2)
    print_with_sleep("Let the fun begin!", 1)

def ask_to_play_again():

    """ This function asks user/player if he/she wishes to replay"""
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()

    # Create a decision making process
    if response == 'y':
        run_game()
    else:
        print("Hope you enjoyed the game !. See you next time :)")

# Define a function for generating random words for the user to guess.
def select_random_word():
    """ This function generates the word the user will attempt guessing"""
    words = ["Horse", "Pony", "Saddle", "Bridle", "Girth", "Equine"]
    return random.choice(words).lower()

# Define function to run the gamey
def run_game():
    # Set guess word to get_word function for a random word to be generated
    word = select_random_word()
    # Initiate an empty list for guessed letter
    guessed_letters = []
    # Initiate a counter for number of tries by the user
    total_attempts_left = 6
    # Set inital guess to false
    user_successfully_guessed = False

    # Print an empty line
    print()
    # Initate a while loop and create decisions
    # Also a create decisions for if user inputs a wrong entry
    # Deduct attempts each user fails to guess incorrectly
    while user_successfully_guessed == False and total_attempts_left > 0:
        print('You have ' + str(total_attempts_left) + ' attempts')
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
                total_attempts_left -=1
                hangman_pic(total_attempts_left)
            elif guessed_letter in word:
                print('Super that letter is in the word')
                guessed_letters.append(guessed_letter)
                hangman_pic(total_attempts_left)
        else:
            print('Please enter only one Letter per try')
            total_attempts_left -=1
        # print letter or dash under hangman pic
        result_letters_list = []
        if user_successfully_guessed == False:
            for letter in word:
                if letter in guessed_letters:
                    result_letters_list.append(letter)
                else:
                    result_letters_list.append('_')

            print(" ".join(result_letters_list))


        if "".join(result_letters_list) == word:
            print()
            user_successfully_guessed = True
            print("Well Done you guessed the right word :)")
            print("-------------------------------------------")

        elif total_attempts_left == 0:
            print()
            print("-------------------------------------------")
            print("Opps! You ran out of guesses, Hard Luck !!")
            print("The correct word was: ", word)
            print("-------------------------------------------")

    #Initiate play_again function if user wishes to continue
    ask_to_play_again()

def start_game():
    show_greeting_and_take_username()
    run_game()


#Full program run
start_game()