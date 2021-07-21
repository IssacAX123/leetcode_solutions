grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

grid2 = [[1]]


def get_perimeter_issac(grid):
    permimeter = 0
    for row in range(len(grid)):
        for column, value in enumerate(grid[row]):
            if value == 1:
                if column < len(grid[row]) - 1:
                    if grid[row][column + 1] == 0:
                        permimeter += 1
                else:
                    permimeter += 1
                if column > 0:
                    if grid[row][column - 1] == 0:
                        permimeter += 1
                else:
                    permimeter += 1

                if row < len(grid) - 1:
                    if grid[row + 1][column] == 0:
                        permimeter += 1
                else:
                    permimeter += 1
                if row > 0:
                    if grid[row - 1][column] == 0:
                        permimeter += 1
                else:
                    permimeter += 1
    return permimeter


def get_perimeter_issac_2(grid, permimeter=0, seen=[], row_i=0, column_i=0):
    if not seen:
        found = False
        row = 0
        column = 0
        while not found:
            value = grid[row][column]
            if value == 1:
                seen.append((row, column))
                row_i = row
                column_i = column
                break
            if column == len(grid[row]):
                column = 0
                row += 1
            else:
                column += 1


    if column_i < len(grid[row_i]) - 1 and grid[row_i][column_i + 1] == 1 and (row_i, column_i + 1) not in seen:
        seen.append((row_i, column_i + 1))
        permimeter += get_perimeter_issac_2(grid, permimeter, seen, row_i, column_i + 1)
    else:
        permimeter += 1

    if column_i > 0 and  grid[row_i][column_i - 1] == 1 and (row_i, column_i - 1) not in seen:
        seen.append((row_i, column_i - 1))
        permimeter += get_perimeter_issac_2(grid, permimeter, seen, row_i, column_i - 1)
    else:
        permimeter += 1

    if row_i < len(grid) - 1 and grid[row_i + 1][column_i] == 1 and (row_i + 1, column_i) not in seen:
        seen.append((row_i + 1, column_i))
        permimeter += get_perimeter_issac_2(grid, permimeter, seen, row_i, column_i + 1)
    else:
        permimeter += 1

    if row_i > 0 and grid[row_i - 1][column_i] == 1  and (row_i - 1, column_i) not in seen:
        seen.append((row_i - 1, column_i))
        permimeter += get_perimeter_issac_2(grid, permimeter, seen, row_i, column_i - 1)
    else:
        permimeter += 1
    return permimeter


def get_perimeter_online(grid):
    visit = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0
        visit.add((i, j))
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return dfs(i, j)

print(get_perimeter_issac_2(grid2))
