"""Consider the problem below. We have given a sequence of characters,
and we want to extract from it all the substrings of length n in the order they
appear in the sequence.
For example, from a sequence of characters 1 python ' we can extract a 3-
digit series:
['pyt', 'yth', 'tho', 'hon']
or 4-digit:
['pyth', 'ytho', 'thon']
Implement a function called get_siices( ) that takes two arguments:
• sequence - the sequence of characters to be processed
• length - length of the substrings to be extracted from the sequence
If the value of the length argument is less than 1, raise the ValueError with
the message:
'The length cannot be less than 1.'
If the value of the length argument is greater than the length of the given
sequence, raise the ValueError with the message:
'The length cannot be greater than sequence.'"""

def get_slices(sequence, length):
    if length < 1:
        raise ValueError("The length cannot be less than 1")
    if length > len(sequence):
        raise ValueError("The length cannot be greater than sequence")
    slices = []
    for i in range(0, len(sequence) - length + 1):
        slices.append(sequence[i:i+length])

    return slices

print(get_slices("esmartdata", 5))