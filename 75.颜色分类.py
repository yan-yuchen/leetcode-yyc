#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针，p1为0与1的边界，p2为1与2的边界
        p1,p2=0,len(nums)-1
        i=0

        while i <= p2:
            if nums[i]==0:
                nums[i],nums[p1]=nums[p1],nums[i]
                p1=p1+1
                i=i+1
            elif nums[i]==2:
                nums[i],nums[p2]=nums[p2],nums[i]
                p2=p2-1
            else:
                i=i+1
# @lc code=end

