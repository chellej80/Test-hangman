import random

# List of words.
word_list = ['horse', 'door', 'song', 'rip']

# The word to be found.
word = random.choice(word_list)
# Guessed word
guessed_word = list('*'*len(word))
# guessed letters
guessed_letters = []


# function to replace '*' with the guessed letter.
def replace(guess):
    # Starting the game
    print('Entering the Game')
    print('word = {}\n'.format(''.join(guessed_word)))


# Getting the no.of attempts to find the word from the user.
chance = 0
while not int(chance) in range(1, 16):
    turn = 1

# Guessing begins
while turn <= chance:
    # prints the word and the guessed letters.
    print('\nword = ', '' .join(guessed_word))
    print('Guessed Letters: ', ','.join(guessed_letters))
    guess = input("turn {}\t".format(turn))

# Executed when the letter has been already guessed.
    if guess in guessed_letters:
        print("Already Guessed\n")
        continue
    guessed_letters.append(guess)
    # Executed when the user finds the entire word.
    if guess == word:
        # Executed when the user guesses the letters in the word.
        if guess in word and len(guess) != 0:

            # User looses the Game.
            print('Game Over\nYou Loose\nThe word is "{}"'.format(word))
            exit(0)
