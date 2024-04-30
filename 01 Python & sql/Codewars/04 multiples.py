'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

'''

def sum_of_multiples(n):
    if n < 0:
        return 0  # Return 0 for negative numbers

    total_sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum

# Example usage:
print(sum_of_multiples(10))  # Output: 23 (3 + 5 + 6 + 9)
print(sum_of_multiples(20))  # Output: 78 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18)
print(sum_of_multiples(-5))  # Output: 0 (Negative input)