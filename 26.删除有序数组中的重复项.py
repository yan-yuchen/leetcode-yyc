#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针算法
        slow, fast = 0, 1

        while fast < len(nums):
            if(nums[slow] == nums[fast]):
                fast = fast+1
            else:
                nums[slow+1] = nums[fast]
                slow = slow+1
                fast = fast+1

        return slow+1


# @lc code=end
