def check_sudoku(grid):
    #CHECKING LINES
    for i in range(9):
        line = grid[i]
        sorted_line = sorted(line) #Sorting to easily check if doubles
        for k in range(8):
            if sorted_line[k] >= sorted_line[k+1]:
                return False

    #CHECKING COLUMNS
    for j in range(9):
        column = [grid[i][j] for i in range(9)]
        sorted_col = sorted(column) #Sorting to easily check if doubles
        for k in range(8):
            if sorted_col[k] >= sorted_col[k+1]:
                return False

    return True
