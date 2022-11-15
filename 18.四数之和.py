#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start

# 和之前三数之和思路一样，在三数之和的基础上多加一层循环
# i，j，左右指针l，r确定一个数
# 与三数之和操作类似，枚举每两个数，表示该数nums[i]和nums[j]已被确定，
# 在排序后的情况下，通过双指针l，r分别从左边l = i + 1和右边n - 1往中间靠拢，
# 找到nums[i] + nums[j] + nums[l] + nums[r] == target的所有符合条件的搭配
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):

                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1

                while(l < r):
                    # 若sum < target，则l往右走，使sum变大
                    if(nums[i]+nums[j]+nums[l]+nums[r] < target):
                        l = l+1
                    # 若sum > target，则r往左走，使sum变小
                    elif(nums[i]+nums[j]+nums[l]+nums[r] > target):
                        r = r-1
                    else:
                        # 若sum == target，则表示找到了与nums[i]搭配的组合nums[l]和nums[r]，存到ans中
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # 去重
                        while(l < r and nums[r] == nums[r-1]):
                            r = r-1
                        while(l < r and nums[l] == nums[l+1]):
                            l = l+1

                        l = l+1
                        r = r-1

        return res


# @lc code=end
