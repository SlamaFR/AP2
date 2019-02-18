def palindrome(str):
    """
    Détermine si la chaîne de caractère est un palindrome.
    :param str: Chaîne de caractère.
    :return: Booléen du résultat.

    >>> palindrome("patate")
    False

    >>> palindrome("kayak")
    True
    """
    if str[0] == str[-1]:
        if len(str) > 2:
            return palindrome(str[1:len(str) - 1])
        else:
            return True
    else:
        return False
