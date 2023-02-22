#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    dp[i][j] = dp[i][j]+dp[i-1][j]
                if j > 0:
                    dp[i][j] = dp[i][j]+dp[i][j-1]

        return dp[m-1][n-1]
# @lc code=end
