#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m=len(s1),len(s2)
        if len(s3)!=n+m:
            return False
        
        dp=[[False]*(m+1) for _ in range(n+1)]

        s1,s2,s3=' '+s1,' '+s2,' '+s3

        for i in range(n+1):
            for j in range(m+1):
                if i==0 and j==0:
                    dp[i][j]=True
                else:
                    if i!=0 and s1[i]==s3[i+j]:
                        dp[i][j]=dp[i-1][j]
                    if j!=0 and s2[j]==s3[i+j]:
                        dp[i][j]=dp[i][j] | dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

