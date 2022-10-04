"""
File: caesar.py
ID:0711506
Author:王偉誠
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# To defined the range how the new_alphabet move.
secret_number = int(input('Secret number:'))


def main():
    """
    You can input a ciphered word, and this program will decipher the inputted word.
    """
    n = input('What\'s the ciphered string?')
    upper_n = n.upper()
    # To make the program case-insensitive.
    print('The deciphered string is:', new_alpha(upper_n))


def new_alpha(upper_n):
    """
    To decipher the inputted word.
    """
    ans = ''
    for ch in upper_n:
        if ch.isalpha():
            if ALPHABET.find(ch) < 26-secret_number:
                ans += ALPHABET[ALPHABET.find(ch)+secret_number]
            elif ALPHABET.find(ch) >= 26-secret_number:
                ans += ALPHABET[ALPHABET.find(ch)+secret_number-26]
        elif ch == ' ':
            ans += ' '
        else:
            ans += ch
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
