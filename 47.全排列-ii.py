#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        used = [False]*len(nums)
        nums.sort()

        def dfs(step):
            if step == len(nums):
                res.append(path[:])

            for i in range(len(nums)):
                # 在前一题的基础上剪枝即可
                # 如果与前一个元素相等且前一个元素已经使用过，则出现重复
                if i > 0 and used[i-1] and nums[i-1] == nums[i]:
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(step+1)
                    used[i] = False
                    path.pop()

        dfs(0)
        return res


# @lc code=end
