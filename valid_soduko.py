def valid_sudoku(board):
    seen =[]
    for i, row in enumerate(board):
        for j, row_col in enumerate(row):
            if row_col != '.':
                seen = seen + [(row_col,i), (j,row_col),(i/3,j/3, row_col)]
    if len(seen) == len(set(seen)):
        return 1
    return 0
print(valid_sudoku([[1,2,'.'],[1,'.','.'],['.',3,'.']]))
