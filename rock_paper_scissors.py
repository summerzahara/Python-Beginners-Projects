#Rock Paper Scissors
import random
rps = ['rock', 'paper', 'scissors']

def validate_entry(input):
    if input in rps:
        return True
    else:
        return False

def game(): 
    a = input("Player A: ").lower()
    b = random.choice(rps)
    print(b)

    if (validate_entry(a) == True) and (validate_entry(b) == True):
        if (a == 'rock') and (b == 'rock'):
            print("Tie")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'rock') and (b == 'paper'):
            print("Player A Wins!")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'rock') and (b == 'scissors'):
            print("Player A Wins!")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'paper') and (b == 'rock'):
            print("Player A Wins!")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'paper') and (b == 'paper'):
            print("Tie")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'paper') and (b == 'scissors'):
            print("Computer Wins!")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'scissors') and (b == 'rock'):
            print("Computer Wins!")
            print("You: " + a)
            print("Computer: " + b)
        elif (a == 'scissors') and (b == 'paper'):
            print("Player A Wins!")
            print("You: " + a)
            print("Computer: " + b)
        else:
            print("Tie")
            print("You: " + a)
            print("Computer: " + b)
    else:
        print("Error: Invalid Entry")

game()