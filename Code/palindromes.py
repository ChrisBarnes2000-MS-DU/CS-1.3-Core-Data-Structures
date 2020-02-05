#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

# def find_letter(text, start, stop, step):
#     """Looks through text, returning only letters along the way.
#     Yields:
#         (int) index of next letter in text."""
#     for i in range(start, stop, step):
#         if (letter := text[i]).isalpha():
#             yield i


# def is_palindrome_iterative(text):
#     size = len(text)
#     mid = size//2

#     left = find_letter(text, 0, mid, 1)
#     right = find_letter(text, size-1, mid, -1)

#     try:
#         left = next(left_it)
#         right = next(right_it)
#     except StopIteration:
#         return True
#     while left < right:
#         if text[left.lower() != text[right].lower():
#             print("{}:@{} doesn't match {}:@{}".format(
#                 text[i], i, text[(size-1)-i], (size-1)-i))
#             return False
#         left = next(left_it)
#         right = next(right_it)
#     return True


def is_palindrome_recursive(text, left=None, right=None):
    """Recursive function for determining if text is a palindrome."""
    if left is None and right is None:
        ## initialize left and right indices
        left = 0
        right = len(text) - 1
    if left > right:
        ## Base case: left and right indices have overlapped, text must be a palindrome
        return True

    text = text.lower()

    if not text[left].isalpha():
        ## left character isn't a letter; move left index to the right by one
        return is_palindrome_recursive(text, left + 1, right)

    elif not text[right].isalpha():
        ## right character isn't a letter; move right index to the left by one
        return is_palindrome_recursive(text, left, right - 1)

    elif text[left] == text[right]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
