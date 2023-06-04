#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)

        # 在 s 串身上 “挑选” 字符，去匹配 t 串的字符，求挑选的方式数
        # 用d[i][j]表示s的前i个字符包含t前j个字符的个数，状态转移方程需要考虑s的第i个字符和t的第j个字符是否匹配。
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0]=1

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i][j]+dp[i-1][j-1]

        return dp[m][n]
# @lc code=end

