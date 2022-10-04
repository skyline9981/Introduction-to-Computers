"""
File: complement.py
ID:0711506
Author:王偉誠
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def build_complement(upper_n):
    """
    A method to building the complement for the sequence.
    For example, print 'A' for 'T', 'T' for 'A', 'C' for 'G', and 'G' for 'C'.
    """
    complement = ''
    for ch in upper_n:
        if ch == 'A':
            complement += 'T'
        elif ch == 'T':
            complement += 'A'
        elif ch == 'C':
            complement += 'G'
        elif ch == 'G':
            complement += 'C'
    return complement


def main():
    """
    To build a complement for the inputted DNA sequence.
    For example, if you input 'ATCG', it will print 'TAGC'.
    """
    n = input('Please give me a DNA strand and I\'ll find the complement:')
    # To make the program case-insensitive.
    upper_n = n.upper()
    print('The complement of', upper_n, 'is', build_complement(upper_n))


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
