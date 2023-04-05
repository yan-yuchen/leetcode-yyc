#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return True
            
            if nums[mid]>nums[left]: # 左半部分必然有序：
                if nums[left]<=target<nums[mid]: # 如果target在这个范围内，则舍弃右半部分
                    right=mid-1
                else: # 如果target不在这个范围内，舍弃左半部分
                    left=mid+1

            elif nums[mid]<nums[left]: # 右半部分必然有序
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

            else:
                left=left+1

        return False  


# @lc code=end

