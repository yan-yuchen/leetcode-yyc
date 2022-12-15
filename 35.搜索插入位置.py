#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # 二分查找
        # 二分的核心是找出一个分界点，如果左右两段有不同的性质，二分就能给它找出来
        # 二分查找有两种情况
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1

        # 可能target比所有元素都大
        if nums[r] < target:
            return r+1
        else:
            return r

        # l, r = 0, len(nums)-1

        # while l < r:
        #     mid = (l+r+1)//2
        #     if nums[mid] <= target:
        #         l = mid
        #     else:
        #         r = mid-1

        # if nums[r] < target:
        #     return r+1
        # else:
        #     return r

# @lc code=end
