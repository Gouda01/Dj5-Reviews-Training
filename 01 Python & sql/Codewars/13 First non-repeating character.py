'''
DESCRIPTION:
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

* Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

'''

def first_non_repeating_letter(s):
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count occurrences of each character, ignoring case
    for char in s:
        char_lower = char.lower()
        char_count[char_lower] = char_count.get(char_lower, 0) + 1
    
    # Find the first non-repeating character and return its original case
    for char in s:
        if char_count[char.lower()] == 1:
            return char
    
    # If all characters are repeating, return an empty string
    return ""


# Test cases
print(first_non_repeating_letter('stress'))    # Output: 't'
print(first_non_repeating_letter('sTreSS'))    # Output: 'T'
print(first_non_repeating_letter('abba'))      # Output: ''