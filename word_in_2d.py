def word_in_2d(matrix, word):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            return dfs(matrix,i,j,word)

def dfs(matrix,i,j,word):
    if len(word)==0:
        return True
    if i<0 or i>=len(matrix) or j < 0 or j>=len(matrix[0]):
        return False
    res = False
    if matrix[i][j] == word[0]:
        res = dfs(matrix,i+1,j,word[1:]) or dfs(matrix,i,j+1,word[1:]) or dfs(matrix,i-1,j,word[1:]) or dfs(matrix,i,j-1,word[1:])        
    return res

print(word_in_2d([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCCED"))
