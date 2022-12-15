#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) < 1:
            return -1

        # 找到分界点
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r+1)//2
            if nums[mid] > nums[0]:
                l = mid
            else:
                r = mid-1

        # 判断target在前一段还是后一段
        if target >= nums[0]:
            l = 0
        else:
            l = r+1
            r = len(nums)-1

        # 在target所在的一半中，二分查找target
        while l < r:
            mid = (l+r+1)//2
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid

        # 这里写成nums[r], 当数组只有一个元素时, 两个二分查找代码都没有走, 而l在上面被+1, 这时会越界, 而r是length-1还是0, 不会产生越界
        if nums[r] == target:
            return l
        else:
            return -1
# @lc code=end
