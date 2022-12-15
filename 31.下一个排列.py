#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):  # 倒序遍历
            # 寻找最后一个前后是升序的值
            if nums[i] > nums[i-1]:
                # 找到后将i到结尾的值排序至升序
                nums[i:] = sorted(nums[i:])
                # 遍历寻找i到结尾中的最小值与nums[i-1]交换
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                return


# @lc code=end
