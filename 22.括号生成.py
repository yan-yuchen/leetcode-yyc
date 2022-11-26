#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        cur_str=''

        # left，right表示当前左括号的数量与右括号的数量
        def dfs(cur_str,left,right):
            # 达到n后停止dfs
            if left ==n and right==n:
                res.append(cur_str)
                return 

            # 必须保证当前字符串左括号数量大于右括号数量方可继续，否则停止dfs
            # 任意一个子序列，右括号的数目必须小于等于左括号的数目
            if left<right:
                return

            # dfs
            if left<n:
                dfs(cur_str+'(',left+1,right)
            if right<n:
                dfs(cur_str+')',left,right+1)

        dfs(cur_str,0,0)
        return res
# @lc code=end

