#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        p=[]

        def dfs(k,step):
            if k==0:
                res.append(p[:])
                return

            for i in range(step,n+1):
                p.append(i)
                dfs(k-1,i+1) #是i+1保证升序，如[1,4],不会出现[4,1]
                p.pop()

        dfs(k,1)
        return res

# @lc code=end

