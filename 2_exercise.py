"""All natural numbers divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14,
15]. The sum of these numbers is: 51. In this exercise, we treat zero as a
natural number.
Find the sum of all numbers that are divisible by 5 or 7 less than 100"""


def calculate():
    numbers = []
    for number in range(100):
        if number % 5 == 0 or number % 7 == 0:
            numbers.append(number)
    total = sum(numbers)
    return total


print(calculate())
