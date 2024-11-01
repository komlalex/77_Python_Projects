"""Consider a simple number compression algorithm that works as
follows:
111155522500 -> [('1', 4), ('5', 3), ('2', 2), ('5', 1), ('O', 2)]
The algorithm goes from left to right through each digit and
returns a list of two-element tuples. Each tuple consists of a
digit and the number of repetitions of a given digit until the
next, different digit in the number is encountered.
Implement a function called compress () that compresses
number as described above."""
from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))

    return result


# Alternatively
def compres(number):
    return [(key, len(list(group))) for key, group in groupby(str(number))]


print(compress(2233555))
