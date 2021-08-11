from typing import List


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

print(setZeroes_issac(
[[1,1,1],
 [1,0,1],
 [1,1,1]]))