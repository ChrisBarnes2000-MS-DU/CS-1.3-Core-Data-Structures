import re
from itertools import permutations, combinations
from binarytree import BinarySearchTree
from Utils.utils import get_clean_words
from my_set import TreeSet

# def ispalindrome(a):
#     return a[::-1].lower() == a.lower()


# def callpalindrom():
#     palindromes = (word for word in words if ispalindrome(word))
#     print('\n'.join(palindromes))


# def REpalindrome():
#     startwith = "MOON"
#     endwith = "GOLF"
#     cklength = re.compile('.{' + str(len(startwith)) + '}(\n)?$', re.I)
#     # cklength = re.compile('.{' + str(4) + '}(\n)?$', re.I)
#     filename = "/usr/share/dict/words"
#     words = set(x.strip().upper() for x in open(filename) if x.match(cklength))


class wordScramble:
    def __init__(self):
        self.diction_words = get_clean_words('/usr/share/dict/words')
        self.words = []
        self.letters = []
        self.final = ''

    def is_real_word(self, word):
        return word in self.diction_words

    def find_permutation(self, chars, final=False):
        if final is True:
            results = combinations(chars, len(chars))
            for options in results:
                option = (''.join(options))
                # option = permutations(options)
                print(option)
        else:
            words = permutations(chars)
            for word in words:
                # print(word)
                word = (''.join(word))
                if self.is_real_word(word):
                    print(word)
                    if word not in self.words:
                        self.words.append(word)


    def split_to_char(self, letters):
        chars = []
        for char in letters:
            chars.append(char)
        # print("now broken into sperate letters", chars)
        return chars


    def solve_word_jumble(self, letters, circles):
        for item, word in enumerate(letters):
            # print("groups of letters we were given", word)
            chars = self.split_to_char(word)
            self.find_permutation(chars)
            # print(circles[item])
            for pos, circle in enumerate(self.split_to_char(circles[item])):
                # print(circle)
                # spot = self.split_to_char(circle)
                if circle == "O":
                    # print(pos, self.words[item][pos])
                    self.letters.append(self.words[item][pos])

        print(self.words)
        # print(self.letters)
        self.find_permutation(self.letters, final=True)









if __name__ == "__main__":
    descram1 = wordScramble()
    descram2 = wordScramble()
    descram3 = wordScramble()
    # Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his __-______."
    # often   -> t, n
    # kiosk   -> k, i, s
    # immune  -> n
    # cousin  -> s, i
    # fillins     t,n,k,i,s,n,s,i
    letters = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final = ['OO', 'OOOOOO']

    descram1.solve_word_jumble(letters, circles)

    print("\n-------------------\n")

    # Cartoon prompt for final jumble: "What a dog house is: A ____ ___."
    letters = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles = ['____O', '_OO__', '_O___O', 'O____O']
    final = ['OOOO', 'OOO']
    descram2.solve_word_jumble(letters, circles)

    print("\n-------------------\n")

    # Cartoon prompt for final jumble:
    # "A bad way for a lawyer to learn the criminal justice system: _____ and _____."
    letters = ['LAISA', 'LAURR', 'BUREEK', 'PROUOT']
    circles = ['_OOO_', 'O_O__', 'OO____', '__O_OO']
    final = ['OOOOO', 'OOOOO']
    descram3.solve_word_jumble(letters, circles)

    print("\n-------------------\n")
