#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:  # 特判，对于数组长度 n，如果数组长度小于 3，返回[]
            return []
        res = []
        nums.sort()  # 对数组进行排序

        for i in range(len(nums)):

            # 若 nums[i] > 0：因为已经排序好，所以后面不可能有三个数和等于 0，直接返回结果。
            if(nums[i] > 0):
                return res

            # 对于重复元素：跳过，避免出现重复解
            if(i > 0 and nums[i] == nums[i-1]):
                continue

            # 令左指针 L = i+1，右指针 R = n−1，当 L < R 时，执行循环：
            l = i+1
            r = len(nums)-1

            while(l < r):
                # 当 nums[i]+nums[L]+nums[R] == 0，执行循环，
                # 判断左界和右界是否和下一位置重复，去除重复解。并同时将 L, R 移到下一位置，寻找新的解
                if(nums[i]+nums[l]+nums[r] == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    # 这里必须使用while，使用if相当于只会特判一次
                    while(l < r and nums[l] == nums[l+1]):
                        l = l+1
                    while(l < r and nums[r] == nums[r-1]):
                        r = r-1
                    l = l+1
                    r = r-1
                # 若和大于 0，说明 nums[R] 太大，R 左移
                elif(nums[i]+nums[l]+nums[r] > 0):
                    r = r-1
                # 若和小于 0，说明 nums[L] 太小，L 右移
                else:
                    l = l+1

        return res

# @lc code=end
