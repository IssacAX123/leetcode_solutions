from typing import List


# o(m + n) space
def setZeroes_issac(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = []
    columns = []
    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            if c == 0:
                if i not in rows:
                    rows.append(i)
                if j not in columns:
                    columns.append(j)
    for row in rows:
        for j in range(len(matrix[row])):
            matrix[row][j] = 0

    for column in columns:
        for i in range(len(matrix)):
            matrix[i][column] = 0
    for row in matrix:
        print(row)


# o(1) space but not working
def setZeroes_issac_2(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row1 = 1
    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            if c == 0:
                matrix[0][j] = 0
                if i == 0:
                    row1 = 0
                else:
                    matrix[i][0] = 0

    for x, rowv in enumerate(matrix[0]):
        if rowv == 0:
            for y in range(len(matrix)):
                matrix[y][x] = 0

    if row1 == 0:
        for x in range(len(matrix[0])):
            matrix[0][x] = 0

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            for x in range(len(matrix[0])):
                matrix[i][x] = 0

    for row in matrix:
        print(row)


print(setZeroes_issac_2(
    [[0, 1, 2, 0],
     [3, 4, 5, 2],
     [1, 3, 1, 5]]))
