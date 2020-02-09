#!python

def empty_pat(text):
    indexes = []
    for i in range(len(text)):
        indexes.append(i)
    return indexes


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Best Case run time: O(1) pattern empty
    Worst Case run time: O(N) Runs find index it it finds the first match"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern == '': return True
    return find_index(text, pattern) != None

def find_index(text, pattern, index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Best Case run time: O(1) pattern is empty return 0
    Average Case run time: O(i) finds the first matching index and returns it
    Worst Case run time: O(N) can't find any matches runs through hole text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    letters = list(text)
    pat = list(pattern)
    if pattern == '': return 0

    for i in range(index, len(letters)):
        for j in range(0, len(pat)):
            if i+j < len(letters):
                if letters[i+j] != pat[j]:
                    break
                elif j == len(pat)-1:
                    return i
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Best Case run time: O(i) finds the first index and returns
    Average/Worst Case run time: O(N) loops through entire text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    occurrences = []
    i = 0
    if pattern == '': return empty_pat(text)
    
    if contains:
        while i is not None:
            i = find_index(text, pattern, i)
            if i is None:
                break
            occurrences.append(i)
            i += 1
        return occurrences
    else :
        return "There are no Matches"


def is_anagram(word1, word2):
    if len(word1) == 1 and word1 == word2:
        return True
    for letter in word1:
        try:
            two_index = word2.index(letter)
            return is_anagram(word1[1:], word2[: two_index] + word2[two_index+1:])
        except:
            return False


def anagrams(text):
    f = open("/usr/share/dict/words", "r")
    contents = f.read()
    words_list = contents.split("\n")
    f.close()
    anagram_list = []
    for word in words_list:
        if len(text) == len(word) and text != word:
            if is_anagram(text, word):
                anagram_list.append(word)
    return anagram_list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
