# write a small Python program that asks the user for a number and tells them if it is odd or even.
def even_odd_num(num):
    if (num % 2) == 0:
        print(str(num) + " is even.")
    else:
        print(str(num) + " is odd.")

print("Enter an integer: ")
user_input = input()
user_num = int(user_input)
even_odd_num(user_num)