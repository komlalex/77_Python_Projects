"""Consider the problem below. We have an application in which at some
point we get a matrix in the form of a string (an object of the sfr type). For
example, the following string:
string = "4 2 7 15 4 2 6 8"
represents a 3x3 matrix. Each row of the matrix is stored on a separate line.
Each element of a row is separated from another element by a space.
                 It's hard to work with these matrices and perform some additional
operations. We will transform such a matrix into nested lists:
[[4, 2, 7], [1, 5, 4], [2, 6, 8]]
Implement a class named Matrix that takes the matrix as a string in the
_init_( ) method
and sets the value of the instance attribute called matrix as nested lists.
Examples:
[IN]: n = Matrix(13 4\n5 61)
[IN]: n.matrix
[OUT]: [[3, 4], [5, 6]]
[IN]: n = Matrix(13 4\n5 6\n7 8') [IN]: m.matrix
[OUT]: [[3, 4], [5, 6], [7, 8]]
You just need to implement the class. The tests run several test cases to
validate the solution."""


class Matrix:
    """Simple Matrix Class"""

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]


m = Matrix("1 3 4\n5 6 1")

print(m.matrix)

