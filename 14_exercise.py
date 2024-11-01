"""Consider a simple number compression algorithm that works
as follows:
111155522500 -> 114_53_22_51_021
The algorithm goes from left to right through the number and returns an
object of type str. Each encountered digit is stored along with the number of
times that digit repeats until another digit is encountered in the number.
Each such pair is separated by the              character.
Implement a function called compress() that compresses number as
described above.
                      Examples:
[IN]: compress(100000) [OUT]: 'l1_05'
[IN]: compress(9993330) [OUT]: '93_33_01'
[IN]: compress(6540000) [OUT]: '61_51_41_04'"""
from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append(f"{key}{len(list(group))}")
    return "_".join(result)


print(compress(113330066666))
