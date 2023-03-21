#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res=[]
        path=[]

        def dfs(nums,step):
            
            if step==len(nums):
                res.append(path[:])
                return
            
            # 选 nums[i]
            path.append(nums[step])
            dfs(nums,step+1)
            path.pop()

            # 不选 nums[i]
            dfs(nums,step+1)
        
        dfs(nums,0)

        return res
            


# @lc code=end

