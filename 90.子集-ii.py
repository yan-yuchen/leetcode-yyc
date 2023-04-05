#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # 前面和78题一致，最后加了去重
        def dfs(step):
            if step==len(nums):
                res.append(path[:])
                return
            
            path.append(nums[step])
            dfs(step+1)
            path.pop()
            dfs(step+1)

        res=[]
        path=[]
        nums.sort()
        dfs(0)
        
        # 去重
        r=[]
        for x in res:
            if x not in r:
                r.append(x)

        return r
# @lc code=end

