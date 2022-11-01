#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start

# 初始时，左右指针位于左右两端，分别从左向右，从右向左移动
# 体积等于最短的柱子乘以两个柱子之间的距离
# 因此每次遍历移动时，每次需要移动两个柱子之间较短的那个柱子，才有可能使得水的体积变大（因为体积取决于最短木坂）
# 每次遍历时，储存当前最大值，再进行下次移动木坂
class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        left, right = 0, len(height)-1

        while (left < right):
            minlen = min(height[left], height[right])
            # 每次更新结果
            res = max(res, minlen*(right-left))
            # 移动木坂
            if (height[left] < height[right]):
                left = left+1
            else:
                right = right-1

        return res

# @lc code=end
