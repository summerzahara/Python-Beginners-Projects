import random

def guess_input():
    print("Guess a number: ")
    user_input = input()
    user_guess = int(user_input)
    return user_guess

def num_guess():
    n = random.randrange(1,51)
    print("Welcome to the number guess game! Guess a number between 1 and 50. You have 5 guess to find the number! Let's get started!")
    g = guess_input()
    count = 1
    print(str(n))
    if (g > n) and (count < 6):
        print("Your guess is too high!")
        count += 1
        print("Turn: " + str(count))
        g = guess_input()
    elif (g < n) and (count < 6):
        print("Your guess is too low!")
        count += 1
        print("Turn: " + str(count))
        g = guess_input()
    elif count > 6:
        print("You have no more guesses. The number was: " + str(n))
    else:
        print("Your guess is correct! " + str(n) + " was the number!")
        
    
    
num_guess()