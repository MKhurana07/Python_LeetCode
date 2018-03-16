def unique_path(m,n):
    nums = [[1 for j in range(n)] for i in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            nums[i][j] = nums[i-1][j] + nums[i][j-1]
    return nums[m-1][n-1]

def unique_with_obstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    nums = [[1 for i in range(n)] for j in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if not obstacleGrid[i-1][j-1]:
                nums[i][j] = nums[i-1][j] + nums[i][j-1]
    return nums[m-1][n-1]

def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1,m):
        grid[i][0] += grid[i-1][0]
    for j in range(1,n):
        grid[0][j] += grid[0][j-1]
    for i in range(1,m):
        for j in range(1,n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[m-1][n-1]

print(unique_path(3,3))
print(unique_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
