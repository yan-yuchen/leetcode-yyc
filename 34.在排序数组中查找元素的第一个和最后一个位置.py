#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 两个二分查找
        if len(nums) == 0:
            return [-1, -1]

        l, r = 0, len(nums)-1

        # 二分查找右边界
        while l < r:
            mid = (l+r+1)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid-1
        b = r

        if nums[b] != target:
            return [-1, -1]

        # 二分查找左边界
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1
        a = r

        return [a, b]

# @lc code=end
