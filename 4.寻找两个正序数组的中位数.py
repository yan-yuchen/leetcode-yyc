#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = sorted(nums1+nums2)

        if (len(temp) % 2 != 0):
            return temp[len(temp)//2]
        else:
            return (temp[len(temp)//2-1]+temp[len(temp)//2])/2


# @lc code=end
