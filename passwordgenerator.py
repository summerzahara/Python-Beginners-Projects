#7: Password Generator Create a Python program that generates a random password for the user. Make sure your program takes a few inputs from the user:

#How long should the password be? How many characters should there be? Should it have both uppercase and lowercase letters? Should it include numbers and special symbols, too? The best part about this small Python project is that you can actually use it for generating strong passwords for your own user accounts across the Web!
import random
def pass_gen():
    upper_letters = []
    lower_letters = []
    numbers = []
    symbols = []

    all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols_arr = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "?"]

    while len(upper_letters) < 3:
        upper = random.choice(all_letters).upper()
        upper_letters.append(upper)
        #print(str(upper_letters))

    while len(lower_letters) < 3:
        lower = random.choice(all_letters)
        lower_letters.append(lower)
        #print(str(lower_letters))

    while len(symbols) < 3:
        sym = random.choice(symbols_arr)
        symbols.append(sym)
        #print(str(symbols))

    while len(numbers) < 3:
        num = random.randrange(0,10)
        numbers.append(num)
        #print(str(numbers))

    psswrd = upper_letters + lower_letters + numbers + symbols
    random.shuffle(psswrd)
    final = ""
    for x in psswrd:
        if type(x) == "string":
            final += x
        else:
            final += str(x)
    print("Password: " + final)
    return final


pass_gen()
