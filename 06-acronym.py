#6: Acronym An acronym Python program will take a given phrase or text and convert it into its acronym. That is, a word that consists of the first letters of each word in the text. To make your acronym easier to read, go ahead and turn the letters into uppercase with Python. Also, think about how the program will take text as input from the user while separating that user input from the logic itself.

def calc_acronym():
    phrase = input("Enter a Phrase: ")
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    print(acronym)
    return 0

calc_acronym()