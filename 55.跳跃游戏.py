#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 第45题需要返回最小跳跃次数，而本题返回能否跳跃成功即可
        # 若往后的位置能跳到，则前面的位置一定可以跳到
        # 在每一个边界内的位置，拓展边界，一旦边界能拓展超过数组末尾，说明可以达到，反之则无法达到
        far = 0
        for i in range(len(nums)):
            if far < i:
                return False
            far = max(far, i+nums[i])
        return True


# @lc code=end
