"""Consider the palindromic numbers. A palindromic or symmetric number
is a number that does not change when you write its digits in reverse order.
Some examples of palindromic numbers:
• 363
• 2882
• 29492
Implement a function that returns the number of all three-digit palindromic
numbers. Present the solution in the form of a function called calculate( ) .
In response, call
calculate( ) function and print the result to the console.
Expected result:
90

"""


def calculate():
    numbers = []

    for i in range(100, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return len(numbers)


print(calculate())
