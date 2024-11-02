"""Consider the problem below. We have an application in
which at some point we get a matrix in the form of a string (an object
of the sfr type). For example, the following string:
string = "4 2 7 15 4 2 6 8"
represents a 3x3 matrix. Each row of the matrix is stored on a separate
line. Each element of a row is separated from another element by a
space.
It's hard to work with these matrices and perform some additional
operations. We will transform such a matrix into nested lists:
[[4, 2, 7], [1, 5, 4], [2, 6, 8]]
Part of a class named Matrix is implemented:
           class Matrix:
    "Simple Matrix class."
    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in
string.splitlines()]
    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in
self.matrix])
    def row(self, index):
        return self.matrix[index]
Add an implementation of the column ( ) method to the Matrix class
that takes the index as an argument and returns the corresponding
column of the matrix.
An example of calling the Matrix.column() method:
An example of calling the Matrix.column() method:
[IN]: n = Matrix(13 4\n5 61)
[IN]: n.column(O)
[OUT]: [3, 5]
An example of calling the Matrix.column() method:
[IN]: n = Matrix(13 4\n5 6\n7 8')
[IN]: m.column(l)
[OUT]: [4, 6, 8]
You only need to implement the column( ) method. The tests run
several test cases to validate the solution."""


class Matrix:
    def __init__(self, string):
        self.matrix = [[int(item) for item in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return "\n".join([" ".join([str(item) for item in row]) for row in self.matrix])

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [row[index] for row in self.matrix]


mat = Matrix("""1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16""")
print(mat.__repr__())
print(mat.column(0))

