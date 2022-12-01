#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 思路与上一题类似，双指针
        slow = 0
        fast = 0
        while(fast < len(nums)):
            if(nums[fast] != val):
                nums[slow] = nums[fast]
                slow = slow+1
                fast = fast+1
            else:
                fast = fast+1

        return slow
# @lc code=end
