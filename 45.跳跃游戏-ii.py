#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:

        count = 0
        pos = 0
        max_nums = 0

        while pos < len(nums)-1:
            n = nums[pos]

            if pos+n >= len(nums)-1:
                return count+1

            # 每次贪心选择的不是当前选择中最大的元素
            # 而是选择，当前选择中可以到达最远的位置的值，即（元素位置+元素的值）的最大值
            for i in range(1, n+1):
                if nums[i+pos]+i+pos >= max_nums:
                    max_nums = nums[i+pos]+i+pos
                    cur = i

            pos = pos+cur
            count = count+1

            max_nums = 0

        return count

# @lc code=end
