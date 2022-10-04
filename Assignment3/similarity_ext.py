"""
File: similarity_ext.py
ID:0711506
Author:王偉誠
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def search(long_sequence, short_sequence):
    """
    To find the most similar part between the long_sequence and short_sequence.
    """
    # Make the long_sequence change to string.
    str_long = str(long_sequence)
    # Make the short_sequence change to string.
    str_short = str(short_sequence)
    # Length of the short_sequence.
    length = len(str_short)
    max_count = -9999999
    s = ''
    ans = ''
    percent = ''
    li = []
    for i in range(len(str_long) - length + 1):
        s += str_long[i:i + length]
    for j in range(len(str_long) - length + 1):
        count = 0
        for k in range(length):
            ch = s[length*j:length*(j+1)]
            if ch[k] == str_short[k]:
                count += 1
            # To memorize the answer.
            if count > max_count:
                max_count = count
                # Calculate the similarity percent.
                percent = str(count / length * 100) + '%'
                ans = ch
    li.append(ans)
    li.append(percent)
    return li


def main():
    """
    Find the most similar DNA sequence, and print it.
    """
    long_sequence = input('Please give me a DNA sequence to search:')
    # To make the program case-insensitive.
    long_sequence = long_sequence.upper()
    short_sequence = input('What DNA sequence would you like to match?')
    # To make the program case-insensitive.
    short_sequence = short_sequence.upper()
    answer = search(long_sequence, short_sequence)
    print('The best match is', answer[0])
    print('The similar percent is ', answer[1])


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
