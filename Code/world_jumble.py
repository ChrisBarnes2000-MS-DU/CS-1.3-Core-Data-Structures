
"""
TEFON       [ , ,0, ,0]     |   often   -> t, n
SOKIK       [0,0, ,0, ]     |   kiosk   -> k, i, s
NIUMEM      [ , , , ,0, ]   |   immune  -> n
SICONU      [ , , ,0,0, ]   |   cousin  -> s, i


fillins     t,n,k,i,s,n,s,i
prompt      farley rolled on the barn floor because of his ---
answer      [0,0]-[0,0,0,0,0,0] 
"""


def ispalindrome(a):
    return a[::-1].lower() == a.lower()


words = (word.strip() for word in open('/usr/share/dict/words', 'r'))
palindromes = (word for word in words if ispalindrome(word))
print('\n'.join(palindromes))


