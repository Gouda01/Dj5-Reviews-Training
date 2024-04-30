# Sum of Digits / Digital Root :
'''
Given n, take the sum of the digits of n. 
If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.
'''


def digital_root(n):
    x = str(n)  # Convert the number to a string
    r = n  # Initialize the result variable

    while len(x) > 1:
        r = 0  # Reset the result for the next iteration
        for i in range(len(x)):
            r += int(x[i])  # Add each digit to the result
        x = str(r)  # Update the string representation

    return r

print(digital_root(15))