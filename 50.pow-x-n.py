#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0

        res = 1
        if n < 0:
            x, n = 1/x, -n

        while n:
            # 对于n的二进制数如果当前位是1的话，则
            if n % 2 == 1:
                res = res*x
            x = x*x
            # 每次除2取余，即二进制数由低位到高位的当前位
            n = n//2

        return res
# @lc code=end
