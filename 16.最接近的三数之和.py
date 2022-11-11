#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
# 和上一题类似，且不用考虑重复情况，越接近目标即可
# 排序+双指针
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 1e8
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while(l < r):
                tmp = nums[i]+nums[l]+nums[r]
                if(abs(res-target) > abs(tmp-target)):
                    res = tmp
                if(tmp == target):
                    return tmp
                elif(tmp < target):
                    l = l+1
                else:
                    r = r-1
        return res
# @lc code=end
