#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    grid[i][j]=grid[0][0]
                elif i==0:
                    grid[i][j]=grid[i][j]+grid[i][j-1]
                elif j==0:
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                else:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        
        return grid[-1][-1]


# @lc code=end

