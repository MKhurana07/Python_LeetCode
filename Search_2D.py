def search_2D_matrix(matrix, val):
    l = 0
    r = len(matrix)*len(matrix[0]) -1
    m = len(matrix[0])
    while ( l != r):
        mid = (l+r-1)//2
        print(mid, l, r ,m)
        if val < matrix[mid//m][mid%m]:
            r = mid
        elif val > matrix[mid//m][mid%m]:
            l = mid + 1
        elif val == matrix[mid//m][mid%m]:
            return True
    return False

print(search_2D_matrix([[1,2,3],[6,7,9],[10,19,20]],5))
