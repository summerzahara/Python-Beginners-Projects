# Horoscope Create a simple horoscope program that asks the user for their star sign and outputs a fun horoscope for them. 
# Bear in mind that your program should display an error message if the user types in their sign wrong.
def validate_bday():
    valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    while True:
        month = input("Enter your month of birth: ").capitalize()
        if month in valid_months:
            break
        print("Error: invalid month")
    while True:
        bday = input("Enter the day: ")
        day = int(bday)
        if (day < 31) and (day > 1):
            break
        print("Error: invalid day")
    return month, day

def zodiac(birth_month, birth_day):
    #zodiac
    if (birth_month == "March") and (birth_day > 20):
        print("Your Zodiac sign is Aries!")
    elif (birth_month == "April") and (birth_day < 20):
        print("Your Zodiac sign is Aries!")
    elif (birth_month == "April") and (birth_day > 19):
        print("Your Zodiac sign is Taurus!")
    elif (birth_month == "May") and (birth_day < 21):
        print("Your Zodiac sign is Taurus!")
    elif (birth_month == "May") and (birth_day > 20):
        print("Your Zodiac sign is Gemini!")
    elif (birth_month == "June") and (birth_day < 21):
        print("Your Zodiac sign is Gemini!")
    elif (birth_month == "June") and (birth_day > 20):
        print("Your Zodiac sign is Cancer!")
    elif (birth_month == "July") and (birth_day < 23):
        print("Your Zodiac sign is Cancer!")
    elif (birth_month == "July") and (birth_day > 22):
        print("Your Zodiac sign is Leo!")
    elif (birth_month == "August") and (birth_day < 23):
        print("Your Zodiac sign is Leo!")
    elif (birth_month == "August") and (birth_day > 22):
        print("Your Zodiac sign is Virgo!")
    elif (birth_month == "September") and (birth_day < 23):
        print("Your Zodiac sign is Virgo!")
    elif (birth_month == "September") and (birth_day > 22):
        print("Your Zodiac sign is Libra!")
    elif (birth_month == "October") and (birth_day < 23):
        print("Your Zodiac sign is Libra!")
    elif (birth_month == "October") and (birth_day > 22):
        print("Your Zodiac sign is Scorpio!")
    elif (birth_month == "November") and (birth_day < 22):
        print("Your Zodiac sign is Scorpio!")
    elif (birth_month == "November") and (birth_day > 21):
        print("Your Zodiac sign is Sagittaruis!")
    elif (birth_month == "December") and (birth_day < 22):
        print("Your Zodiac sign is Sagittarius!")
    elif (birth_month == "December") and (birth_day > 21):
        print("Your Zodiac sign is Capricorn!")
    elif (birth_month == "January") and (birth_day < 20):
        print("Your Zodiac sign is Capricorn!")
    elif (birth_month == "January") and (birth_day > 19):
        print("Your Zodiac sign is Aquarius!")
    elif (birth_month == "February") and (birth_day < 19):
        print("Your Zodiac sign is Aquarius!")
    elif (birth_month == "February") and (birth_day > 18):
        print("Your Zodiac sign is Pisces!")
    elif (birth_month == "March") and (birth_day < 21):
        print("Your Zodiac sign is Pisces!")
    else:
        print("Error")

x, y = validate_bday()
zodiac(x,y)
    
