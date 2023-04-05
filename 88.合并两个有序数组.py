#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k=m+n-1

        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[k]=nums1[m-1]
                m=m-1
            else:
                nums1[k]=nums2[n-1]
                n=n-1
            k=k-1
        # 当nums2比nums1长的时候，需要把nums2剩下的补到前面。nums1比nums2长的话则无需操作
        nums1[:n]=nums2[:n]
        
# @lc code=end

