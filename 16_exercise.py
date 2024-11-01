"""Consider a simple number compression algorithm that works as
follows:
111155522500 -> 114_53_22_51_021
The algorithm goes from left to right through the number and returns an
object of str type. Each encountered digit is stored along with the number of
times that digit repeats until another digit is encountered in the number.
Each such pair is separated by the character.
A function called compress() is implemented that compresses a number as
described above:
from itertools import groupby
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)
 Implement a function called decompress( ) that decompresses the
expression to a number.
Examples:
[IN]: decompress('14_53_22_51_02') [OUT]: 111155522500
[IN]: decompress(111_03_51_031) [OUT]: 10005000"""


def decompress(string):

    my_list = string.split("_")

    result = [(item[0], item[1:]) for item in my_list]
    result = [key * int(count) for key, count in result]
    result = "".join(result)
    return int(result)


print(decompress("14_53_22_51_02"))
