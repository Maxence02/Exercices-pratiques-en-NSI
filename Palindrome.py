def cree_palindrome(mot, palindrome):
    m = ''
    mot_inverse = mot[::-1]
    m = mot + palindrome + mot_inverse 
    return m


# tests

assert cree_palindrome("ka", "y") == 'kayak'
assert cree_palindrome("ser", "") == 'serres'
assert cree_palindrome("r", "ada") == 'radar'
assert cree_palindrome("ar", "fettttef") == 'arfettttefra'
