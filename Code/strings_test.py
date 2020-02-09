#!python

from strings import contains, find_index, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern

        assert contains('hyped', '') is True
        assert contains('hyped', 'h') is True
        assert contains('hyped', 'y') is True
        assert contains('hyped', 'p') is True
        assert contains('hyped', 'e') is True
        assert contains('hyped', 'd') is True
        assert contains('hyped', 'hy') is True
        assert contains('hyped', 'yp') is True
        assert contains('hyped', 'pe') is True
        assert contains('hyped', 'ed') is True
        assert contains('hyped', 'hyp') is True
        assert contains('hyped', 'ype') is True
        assert contains('hyped', 'ped') is True
        assert contains('hyped', 'hype') is True
        assert contains('hyped', 'yped') is True
        assert contains('hyped', 'hyped') is True
        assert contains('yooooooo', 'o') is True
        assert contains('yooooooo', 'ooooo') is True

        assert contains('edede', 'de') is True  # double pattern
        assert contains('\n', 'abc') is False  # escape character
        assert contains('\n', '\n') is True  # two escape characters
        assert contains('', '') is True  # double blank

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last

        assert contains('hyped', 'l') is False
        assert contains('hyped', ' ') is False
        assert contains('hyped', 'hhy') is False
        assert contains('hyped', 'ypod') is False

        assert contains('n', '\n') is False  # escape characters
        assert contains('[[]]', '[[[]]') is False  # non alpha characters

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix

        assert contains('arrrrrrrg', 'rg') is True 
        assert contains('arrrrrrrg', 'rrr') is True
        assert contains('arrrrrrrg', 'rrrrg') is True
        assert contains('arrrrrrrg', 'rrrrrrg') is True
        assert contains('oooooooooh', 'oooh') == True
        assert contains('oooooh', 'oooh') == True
        # random non alpha characters
        assert contains('[][][]][][[][][][][[[]]]]]]', ']]]]') == True
        assert contains(
            '..,,.. ,,.,. ,., ,,,,.... ,,,,,,..... .,.', ' .,.') == True  # obscure and space

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern

        assert find_index('hello there', '') == 0
        assert find_index('hello there', ' ') == 5
        assert find_index('hello there', 'h') == 0
        assert find_index('hello there', 'e') == 1
        assert find_index('hello there', 'he') == 0
        assert find_index('General Kenobi', 'Kenobi') == 8
        assert find_index('General Kenobi', 'en') == 1
        assert find_index('General Kenobi', 'obi') == 11
        assert find_index('General Kenobi', 'l K') == 6

        assert find_index('oooooooooh', 'oooh') == 6
        assert find_index('oooooh', 'oooh') == 2

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last

        # larger pattern than input
        assert find_index('ooooooooo', 'oooooooooo') is None
        assert find_index('...', ',') is None

        assert find_index('hello there', 'their') is None
        assert find_index('hello there', "they're") is None
        assert find_index('hello there', 'hewwo') is None
        assert find_index('hello there', 'hiya there') is None

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix

        assert find_index('heyheymommasaidthewayyoumove', 'ymom') == 5
        assert find_index("if there's a will, there's a way", "there's a way") == 19
        assert find_index('arrrrrrrg', 'rg') == 7
        assert find_index('arrrrrrrg', 'rrr') == 1
        assert find_index('arrrrrrrg', 'rrrrg') == 4
        assert find_index('arrrrrrrg', 'rrrrrrg') == 2

        assert find_index('asdfasvazasdf', '') == 0  # empty pattern
        # repeating patterns
        assert find_index('uuummummmuuummmm', 'uuummm') == 9
        assert find_index('ooo', 'oo') == 0  # sorta strange pattern

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern

        assert find_all_indexes('hello there', '') == [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert find_all_indexes('hello there', ' ') == [5]
        assert find_all_indexes('hello there', 'h') == [0, 7]
        assert find_all_indexes('hello there', 'e') == [1, 8, 10]
        assert find_all_indexes('General Kenobi', 'Kenobi') == [8]
        assert find_all_indexes('General Kenobi', 'obi') == [11]
        assert find_all_indexes('General Kenobi', 'l K') == [6]

        assert find_all_indexes('\nhi\n', '\n') == [0, 3]  # escape characters
        assert find_all_indexes('🥑 🥑', '🥑') == [0, 2]


    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last

        assert find_all_indexes('hello there', 'their') == []
        assert find_all_indexes('hello there', 'low') == []
        assert find_all_indexes('hello there', 'help') == []

        assert find_all_indexes('axx', 'xz') == []  # sending characters
        assert find_all_indexes('asd', 'asdasd') == []  # longer pattern
        assert find_all_indexes('abc', '') == [
            0, 1, 2]  # all indexes in string if char is empty

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix

        assert find_all_indexes('General Kenobi', 'en') == [1, 9]
        assert find_all_indexes('hello there', 'he') == [0, 7]


if __name__ == '__main__':
    unittest.main()
