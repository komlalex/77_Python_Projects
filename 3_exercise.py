"""Consider the Fibonacci sequence. It is a sequence of natural
numbers defined recursively as follows:
• the first element of the sequence is 0
• the second element of the sequence is 1
• each next element of the sequence is the sum of the previous two
elements
The beginning of the Fibonacci sequence:
Find the sum of all even elements of the Fibonacci sequence with
values less than 1,000,000 (1 million)"""


def calculate():
    total = 0
    a = 0
    b = 1
    while a < 1000000:
        if a % 2 == 0:
            total += a

        a, b = b, a + b
    return total


print(calculate())
