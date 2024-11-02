"""Consider the problem below. We have an application in which at some
point we get a matrix in the form of a string (an object of the sfr type). For
example, the following string:
string = "4 2 7 15 4 2 6 8"
represents a 3x3 matrix. Each row of the matrix is stored on a separate line.
Each element of a
row is separated from another element by a space.
It's hard to work with these matrices and perform some additional
operations. We will transform such a matrix into nested lists:
[[4, 2, 7], [1, 5, 4], [2, 6, 8]]
Part of a class named Matrix is implemented:
class Matrix:
    "Simple Matrix class."
    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]
              Add an implementation of the _rePr_( ) method to the Matrix class
that is a formal representation of a Matrix object."""


class Matrix():
    "Simple Matrix Class"

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return "\n".join([(" ".join([str(i) for i in row])) for row in self.matrix])


matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
print(matrix.__repr__())
