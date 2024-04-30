# Persistent Bugger :

'''
If we list all the natural nbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the nber passed in.

Additionally, if the nber is negative, return 0.

Note: If the nber is a multiple of both 3 and 5, only count it once.

'''

def persistence(n):
    if n < 10:
        return 0  # Single-digit nbers have a persistence of 0

    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1

    return steps

# Example usage:
print(persistence(39))  # Output: 3 (3*9 = 27, 2*7 = 14, 1*4 = 4)
print(persistence(999))  # Output: 4 (9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, 1*2 = 2)
print(persistence(4))  # Output: 0 (4 is already a one-digit nber)