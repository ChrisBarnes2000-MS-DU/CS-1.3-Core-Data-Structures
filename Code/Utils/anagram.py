from collections import Counter
from utils import get_clean_words
import dictionary_words
import rearrange
import random
import sys

def anagram(params):
    for val in range(len(params) - 1, 0, -1):
        j = random.randint(0, val + 1)
        params[val], params[j] = params[j], params[val]
    return params

# Check if two strings are anagrams
def check_anagram(input1, input2):
    return Counter(input1) == Counter(input2)

def main():
    if len(sys.argv) == 2:
        #Open dictionary/words file list to check if word is real before making anagram
        words_list = get_clean_words("/usr/share/dict/words")
        #Get the word via the terminal input
        word = sys.argv[1]
        print(word)
        #Check if word is in the dictionary/words file
        for list_word in words_list:
            if list_word == word:
                #Turn the word string into a list
                letter_list = list(word)
                #Create the anagram of the word as a list
                ang_word = ''.join(anagram(letter_list))
                print(ang_word)
        if check_anagram(word, ang_word):
                print("These are anagrams!!")
        else:
            print("They are not anagrams :(")
    else:
        print("Try again with 1 argument: he number of words to give!")

if __name__ == "__main__":
    main()
