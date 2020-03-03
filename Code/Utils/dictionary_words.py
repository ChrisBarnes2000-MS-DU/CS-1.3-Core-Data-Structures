import sys
import random
from utils import get_clean_words

def get_random_word(num):
    words_list = get_clean_words("/usr/share/dict/words")
    word = words_list[random.randint(0, len(words_list)-1)]
    return word

def make_sentence():
    sentence = ""
    for i in range(0, num):
        word = get_random_word(num)
        #print(i+1, word)
        if i == 0:
            sentence = word.capitalize()
        elif i != num - 1:
            sentence += " " + word
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            sentence += random.choice(punctuation)

    #output your sentence
    #print(sentence + "\t: " + str(num) + " words")

if __name__ == "__main__":
    #The program only accepts one argument: the number of words to be selected.
    if len(sys.argv) != 2:
        print("Try again with 1 argument: the number of words to give!")
    else:
        #All parameters except the number of words will be hard-coded.
        num = int(sys.argv[1])
        #put the number of words requested together into a "sentence"
        make_sentence()