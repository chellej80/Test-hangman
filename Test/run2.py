word = "horse"
guessedLetters = ""
counter = 6

# loops until player make too many failed attempts
while counter > 0:
    guess = input("Enter a letter: \n")

    if guess in word:
        print(f"Correct the letter: {guess} is in the word")
    else:
        counter -= 1
        print(f"Incorrect {counter} turn(s) left")

    guessedLetters = guessedLetters + guess
    wrongLetterCount = 0

    for letter in word:
        if letter in guessedLetters:
            print(f" {letter}", end = "")
        else:
            print("_", end = "")
            wrongLetterCount += 1
    print("")
    if wrongLetterCount == 0:
        print(f"Well done ! The secret word was: {word}. You Won") 
        break
else:
    print(f"Sorry you didn't win this time")