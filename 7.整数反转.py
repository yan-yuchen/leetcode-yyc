#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if (x > 0):
            flag = 1
        else:
            flag = -1

        x = abs(x)
        res = 0

        while (x > 0):
            res = res*10+x % 10
            x = x//10
            # 整除

        if res >= 0x7fffffff:
            return 0

        return res*flag

# @lc code=end
