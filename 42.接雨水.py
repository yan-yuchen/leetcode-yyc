#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        s, h1, h2 = 0, 0, 0

        for i in range(len(height)):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-1-i])
            s = s+h1+h2-height[i]

        return s-len(height)*h1
# @lc code=end
