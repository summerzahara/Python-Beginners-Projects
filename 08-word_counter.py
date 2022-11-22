import collections
import string
from pprint import pprint


def word_counter(txt):
    remove_punc = str.maketrans("", "", string.punctuation)
    with open(txt, "r") as file:
        read_file = file.read().lower().translate(remove_punc).split()
        count = collections.Counter(read_file)
        pprint(count)
        return 0


def o_file(txt):
    with open(txt, "r") as file:
        read_file = file.read()
        print(read_file)
        return 0


#o_file("i_have_a_dream.txt")

word_counter("i_have_a_dream.txt")

def remove():
    txt = "Hello Sam!"
    mytable = txt.maketrans("S", "P")
    print(txt.translate(mytable))

# remove()
