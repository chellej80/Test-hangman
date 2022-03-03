import random
import time

easy = ['pear', 'mango', 'apple']
hard = ['hawkeye', 'robin']
guesslist = []
guesses = []
playGame = True
category = ""
continueGame = "Y"

name = input("Enter your name \n")
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)
print("The objective of the game is to guess")
time.sleep(1)
print("Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)

while True:
    # Choosing the Secret word
    while True:
        if category.upper() == 'E':
            secretWord = random.choice(easy)
            break
        elif category.upper() == 'H':
            secretWord = random.choice(hard)
            break
        else:
            category = input("E for Easy / H for Hard; X to exit \n")

        if category.upper() == 'X':
            print("Bye. See you next time!")
            playGame = False
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 2)

        # Utility function to print User Guess List
        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(guesslist))
        # Adding blank lines to userGuesslist to create the blank secret word
        for n in secretWordList:
            guesslist.append('_')
        printGuessedLetter()

        print("The number of allowed guesses for this word is:", attempts)
        # starting the game
        while True:

            print("Guess a letter:")
            letter = input()

            if letter in guesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                guesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            guesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:
                    print("Oops! Try again.")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    printGuessedLetter()
            # Win/loss logic for the game
            joinedList = ''.join(guesslist)
            if joinedList.upper() == secretWord.upper():
                print("Yay! you won.")
                break
            elif attempts == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: " + secretWord.upper())
                break

        # Play again logic for the game
        continueGame = input("Do you want to play again? Y to continue \n")
        if continueGame.upper() == 'Y':
            category = input("E for Easy / H for Hard")
            guesslist = []
            guesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break
