#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        hashmap = {i: i for i in nums if i > 0}

        for i in range(1, len(hashmap)+1):
            if i not in hashmap:
                return i
        return len(hashmap)+1

# @lc code=end
