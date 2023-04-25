#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1

        for m in range(1,n+1): # 枚举长度
            for i in range(1,m+1): # 枚举root节点的位置
                dp[m]=dp[m]+dp[i-1]*dp[m-i] # dp[m]=左子树*右子树

        return dp[n]
    
# @lc code=end

