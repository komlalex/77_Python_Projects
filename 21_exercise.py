""" Let's consider vectors consisting of only ones and zeros. Let us also
assume an additional convention for representing such a vector. For
example, a vector:
U = [0, 1, 1, 0, 1, 0, 1, 0] we will present as a sequence:
‘01101010'
  For the vectors so defined, we can determine the Hamming distance. The
Hamming distance of vectors u and v is the number of elements where the
vectors u and v are different.
Example: The Hamming distance of the vectors '1100100' L ' 1010000' is
equal to 3.
Implement a function called hamming_distance( ) that returns the Hamming
distance of two vectors. To calculate the Hamming distance, the vectors
must be of the same length. If the vectors are of different lengths raise the
ValueError with the following message:
'Both vectors must be the same length.'"""


def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError("Both vectors must be of the same length")

    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1

    return distance


print(hamming_distance("1100100", "1010000"))
