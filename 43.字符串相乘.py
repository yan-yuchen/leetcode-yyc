#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = 0

        for i in range(len(num2)-1, -1, -1):
            res = res+int(num1)*int(num2[i])*(10**(len(num2)-i-1))

        return str(res)
# @lc code=end
