#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 鍥炴枃鏁?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 方法一：直接翻转判断是否相等
        # s = str(x)
        # if (s == s[::-1]):
        #     return True
        # else:
        #     return False

        # 手动翻转数字
        num = x
        res = 0

        if (x < 0):
            return False

        while (num != 0):
            res = res*10+num % 10
            num = num//10

        return res == x

# @lc code=end
