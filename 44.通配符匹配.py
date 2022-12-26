#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        # 初始化
        dp[0][0] = True
        for j in range(1, n+1):     # p以*开头的情况
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        # 状态更新
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':   # 条件1-2
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':                     # 条件3
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]

        return dp[m][n]

# @lc code=end
