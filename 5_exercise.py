"""In number theory, integer factorization is the decomposition of a
composite number into a product of smaller integers. If these factors are
further restricted to prime numbers, the process is called prime
factorization.
Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ... Reminder: The
number 1 is not a prime number.
A number that is greater than 1 and is not a prime is called a composite
number.
Examples of composite numbers: 4, 6, 8, 9, 10, 12, 14, 15, 16, ...
We can break down a composite number into prime factors. For example:
• 15 = 3*5
• 36=2*2*3*3
The largest prime factor for 15 is 5, and for 36 is 3.
Using the previous exercise, implement a function that takes a natural
number as an argument
and returns the greatest prime factor of that number. Present the solution in
the form of a function called calculate() ."""


def calculate(number):
    factors = []
    i = 2
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)

    greatest = max(factors)
    return greatest


print(calculate(13195))
