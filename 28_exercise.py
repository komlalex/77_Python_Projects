"""The exercise includes a file called binary.txt containing numbers in
binary system (each number is on a separate line.):
0111111000100101
1010111100000010
0010110000011010
1111000101111100
0100101101000110
0001001000011110
0000011011010101
0010100001101000
0100001100001101
0001111111000001
0111101000000100
1010100010001011
0010001000011000
0100010011110110
0010010011111011
Implement a function called binary_to_int( ) that reads the included
binary.txt file and converts the given numbers to decimal system. Return the
numbers as a list.
"""


def binary_to_int():
    with open("binary.txt", "r") as fh:
        content = fh.read()
        binaries = content.split()
        integers = [int("0b" + binary, base=2) for binary in binaries]
        return integers


print(binary_to_int())
