def check_sudoku(grid):
    #CHECKING LINES
    for i in range(9):
        line = grid[i]
        sorted_line = sorted(line)
        print(sorted_line)
        for k in range(8):
            if sorted_line[k] >= sorted_line[k+1]:
                return False

    #CHECKING COLUMNS
    for j in range(9):
        column = [grid[i][j] for i in range(9)]
        sorted_col = sorted(column)
        print(sorted_col)
        for k in range(8):
            if sorted_col[k] >= sorted_col[k+1]:
                return False

    return True


grid_2 = [[8,1,3,9,2,5,7,4,6],[9,5,6,8,4,7,3,1,2],[4,7,2,3,6,1,8,9,5],[6,2,4,7,1,9,5,3,8],[7,9,5,6,3,8,4,2,1],[3,8,1,4,5,2,9,6,7],[2,3,8,1,7,4,6,5,9],[5,4,9,2,8,6,1,7,3],[1,6,7,5,9,3,2,8,4]]
grid_1 = [[1,7,3,5,9,4,8,5,6],[1,3,9,4,6,4,2,9,0],[8,4,0,8,9,2,5,7,8],[6,1,3,7,5,6,3,9,1],[3,4,8,6,1,2,5,4,5],[3,6,2,4,9,7,6,2,5],[8,7,4,5,6,3,1,9,4],[9,5,4,2,8,7,2,6,7],[2,9,5,3,5,4,1,9,8]]

print(check_sudoku(grid_2))
