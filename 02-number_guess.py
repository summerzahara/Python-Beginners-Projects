import random

def guess_input():
    print("Guess a number: ")
    user_input = input()
    user_guess = int(user_input)
    return user_guess

def num_guess():
    n = random.randrange(1,51)
    print("Welcome to the number guess game! Guess a number between 1 and 50. You have 5 guess to find the number! Let's get started!")
    count = 1
    while (count <6):
        print("Turn # " + str(count))
        g = guess_input()
        if (g<0 or g>50):
            print("Enter a valid numver between 1 and 50\n")
        elif (g > n):
            print("Your guess is too high!\n")
            count += 1
        elif (g < n):
            print("Your guess is too low!\n")
            count += 1
        else:
            print("Your guess is correct! " + str(n) + " was the number!")
            break
    print("You have no more guesses. The number was: " + str(n))
        
    
    
num_guess()