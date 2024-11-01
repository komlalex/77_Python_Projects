"""Greatest Common Divisor (GCD) of two integers - this is the largest
natural number that divides both of these numbers without a remainder.
For example, for numbers 32 and 48, the greatest common divisor is 16,
which we can write
GCD(32, 48) = 16 .
Implement a function called greatest_common_divisor() that determines the
greatest common divisor of two numbers.
Implement a function called greatest_common_divisor() that determines the
greatest common divisor of two numbers."""


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


print(greatest_common_divisor(48, 32))
