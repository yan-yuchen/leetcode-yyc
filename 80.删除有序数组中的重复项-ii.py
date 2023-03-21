#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 哈希表
        hashMap = Counter(nums)
        for k, v in hashMap.items():
            while v > 2:
                nums.remove(k)
                v = v - 1
        return len(nums)
# @lc code=end

