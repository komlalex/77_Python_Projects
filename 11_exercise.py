"""Consider the palindromic numbers. A palindromic or symmetric
number is a number that does not change when you write its digits in
reverse order.
Some examples of palindromic numbers:
• 363
• 2882
• 29492
Implement a function called is_palindrome( ) that checks if the passed
number is palindromic decimal and binary.
  For example, the number 99 is a palindromic number and its binary
notation 1100011 is also a palindrome. When these conditions are
met, the function returns True, otherwise False."""


def is_palindromic(n):
    if str(n) != str(n)[::-1]:
        return False

    binary_number = bin(n)[2:]

    return binary_number == binary_number[::-1]


print(is_palindromic(99))
