def set_matrix_zero(matrix):
    cols=[]
    for i in range(len(matrix)):
        for k,val in enumerate(matrix[i]):
            if val == 0:
                matrix[i] = [0 for j in range(len(matrix[i]))]
                cols.append(k)
    for i in range(len(matrix)):
        for j in cols:
            if j<len(matrix[i]):matrix[i][j]=0

    return matrix

print(set_matrix_zero([[1,2,3],[0,9,1,7],[9,0,1]]))

def set_0(matrix):
    rowset = set()
    colset= set()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                rowset.add(r)
                colset.add(c)
    for c in colset:
        for r in range(len(matrix)):
            matrix[r][c] = 0

    for r in rowset:
        for c in range(len(matrix[r])):
            matrix[r][c] = 0

    return matrix
print(set_0([[1,2,3],[0,9,1,7],[9,0,1]]))
