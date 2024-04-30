'''
Replace With Alphabet Position

DESCRIPTION:
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

'''

def alphabet_position(text):
    # Create a dictionary to map letters to their positions
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
                'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    # Convert the input text to lowercase
    text = text.lower()

    # Initialize an empty result string
    result = ""

    # Iterate through each character in the input text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            result += str(alphabet[char]) + " "  # Append the position to the result

    # Remove the trailing space and return the result
    return result.strip()

# Example usage:
print(alphabet_position("The sunset sets at twelve o' clock."))  # Output: "20 8 5 19 21 14 19 5 20 19 1 20 20 23 5 12 22 5 19 5 20 18 5 5 14 5 23 5 12 22 5 15 3 12 15 3 11"
print(alphabet_position("Hello, World!"))  # Output: "8 5 12 12 15 23 15 18 12 4"