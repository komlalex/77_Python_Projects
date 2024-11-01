"""A prime number is a natural number greater than 1 that is not a product
of two smaller natural numbers.
Examples of prime numbers: 2, 3, 5, 7, l1, 13, 17, 19, ...
Implement a function called is_prime( ) that takes a natural number as an
argument and checks if it is a prime number. In the case of a prime number,
the function returns True, otherwise False."""


def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True


print(is_prime(3))

