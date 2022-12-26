#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        vis = [False]*len(nums)

        def dfs(step):
            if step == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not vis[i]:
                    vis[i] = True
                    path.append(nums[i])
                    dfs(step+1)
                    vis[i] = False
                    path.pop()

        dfs(0)
        return res

# @lc code=end
