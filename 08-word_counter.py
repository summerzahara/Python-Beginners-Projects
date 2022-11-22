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


word_counter("i_have_a_dream.txt")
