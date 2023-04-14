#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(1,n):
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    dp[i+1]=dp[i-1]
                else:
                    return 0
            else:
                if s[i-1]=='1' or (s[i-1]=='2' and '1'<=s[i]<='6'): # 可以自己单独解码也可以和上一位组合解码，所以s[i+1]=s[i]+s[i-1]
                    dp[i+1]=dp[i]+dp[i-1]
                else:
                    dp[i+1]=dp[i]

        return dp[n]
# @lc code=end

