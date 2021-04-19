"""
Kata description:

Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)

Matrix = array of n length whose elements are n length arrays of integers.

3x3 example:

sum_diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7

"""


def sum_diagonals(matrix):
    suma = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                suma += matrix[i][j]
        matrix[i].reverse()
        for j in range(len(matrix[i])):
            if i == j:
                suma += matrix[i][j]
    return suma


if __name__ == "__main__":
    print(sum_diagonals([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]))
