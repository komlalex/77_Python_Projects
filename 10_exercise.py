"""A prime number is a natural number greater than 1 that is not a
product of two smaller natural numbers.
Examples of prime numbers: 2, 3, 5, 7, l1, 13, 17, 19, ...
The prime number in position one is 2. The prime number in position
two is 3. The prime number in position three is 5. Implement a
function that returns a prime number at position 100.
"""


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


def calculate():
    number = 2
    counter = 0

    while True:
        if is_prime(number):
            counter += 1
            if counter == 100:
                return number
        number += 1


print(calculate())
