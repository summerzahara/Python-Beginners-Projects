# Hangman Hangman is one of the best Python projects for beginners who want a bit of a challenge. The game is about guessing a random word with a limited number of guesses. Although Hangman may sound rather simple, you need to consider a few key points, such as:
    # 1) You need to set a maximum limit for guesses.
    # 2) The player needs to be notified about the remaining number of guesses.
    # 3) Your player needs to be able to input their guesses.
    # 4) To get started, you need a way to generate random words to be guessed. The best way is to simply create a separate text file where you store the words or short phrases.

# This Python project will probably take you a bit longer, but it’s great practice. You will have to think about random choice, variables, boolean values, inputs and outputs, strings, length, and much more.

import random


#user guess
#limit number of guesses (head, torso, r-arm, l-arm, r-leg, l-leg = 6)
def hangman():
    ## Generate the word
    words = ["align", "bacon", "civil", "daddy", "eager", "fable", "grimy", "habit", "icily", "jaunt", "kneel", "label", "media", "naive", "obese", "plane", "quest", "resin", "semen", "token", "union", "vague", "wharf", "yacht", "zebra"]

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    WORD = random.choice(words)
    #print(WORD)

    ## Calculate length of word and show player
    word_size = len(WORD)
    display_blanks = "_ "*word_size
    print(display_blanks)

    ##split word into letters
    WORD_split = list(WORD)
    #print(WORD_split)

    count = 0
    incorrect_guess = []
    correct_guess = []
    guessed = []
    with_guess = []
    for element in display_blanks:
        if element.strip():
            with_guess.append(element)
    #print(with_guess)

    while count < 7 and "_" in with_guess:
        guess = input("Guess a letter: ")
    
        if guess in WORD_split:
            print("Correct!")
            correct_guess.append(guess)
            guessed.append(guess)
            n = 0
            for element in WORD:
                if element in guessed:
                    with_guess[n] = element
                    n += 1
                else:
                    with_guess[n] = "_"
                    n += 1
            print(arr_to_word(with_guess))
            count += 1
            print("You have completed " + str(count) + "/7 tries.")
        elif guess in incorrect_guess:
            print(guess + " is already tried")
        elif guess not in letters:
            print(guess + " is not a valid letter")
        else:
            print(guess + " is not in the word!")
            incorrect_guess.append(guess)
            guessed.append(guess)
            print("Guesses: " + str(guessed))
            count += 1
            print("You have completed " + str(count) + "/7 tries.")
    if count < 7:
        print("You Win! The word is " + WORD)
    else:
        print("You Lose. The word was " + WORD)

def arr_to_word(array):
    new = ""

    for x in array:
        new += x
    return new

hangman()


