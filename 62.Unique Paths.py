# This is forward solution
# Backward solutuon is in this video: https://www.youtube.com/watch?v=IlEsdxuD4lY&ab_channel=NeetCode
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m 
        col = n 
        grid= [[1] * col for _ in range (row)]

        for r in range (1 , row):
            for c in range(1, col):
                grid[r][c] = grid[r][c-1] + grid[r-1][c] 

        return grid [-1][-1]
        
