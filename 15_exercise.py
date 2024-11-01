"""Consider a simple number compression algorithm that works
as follows:
111155522500 -> '1....5...2..5.0..'
The algorithm goes from left to right through the number and returns an
object of str type. Each encountered digit is stored along with the number of
dots - the number of times the given digit repeats until it encounters the
next, different digit in the number.
Implement a function called compress() that compresses number as
described above."""
from itertools import groupby


def compress(number):
    result = []

    for key, group in groupby(str(number)):
        result.append(f"{key}{'.' * len(list(group))}")
    return "".join(result)


print(compress(1000040000))
