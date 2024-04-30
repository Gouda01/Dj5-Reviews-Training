'''
Playing with digits :

DESCRIPTION:
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.

Examples:
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

'''

def find_k(n, p):
    # Compute the sum of digits of n raised to consecutive powers
    total_sum = 0
    current_power = p
    for digit in str(n):
        total_sum += int(digit) ** current_power
        current_power += 1

    # Check if k exists
    if total_sum % n == 0:
        k = total_sum // n
        return k
    else:
        return -1

# Example usage:
n1, p1 = 89, 1
print(f"For n = {n1} and p = {p1}, k = {find_k(n1, p1)}")

n2, p2 = 695, 2
print(f"For n = {n2} and p = {p2}, k = {find_k(n2, p2)}")

n3, p3 = 46288, 51
print(f"For n = {n3} and p = {p3}, k = {find_k(n3, p3)}")