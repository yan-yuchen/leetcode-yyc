#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    # 倍增法
    # x << i, 左移相当于 x* 2^i
    # x >> i, 右移相当于 x/ 2^i
    def divide(self, x: int, y: int) -> int:
        is_minus = False
        if (x < 0 and y > 0) or (x > 0 and y < 0):
            is_minus = True

        # 计算y*2^0,y*2^1,y*2^2,...,存到ex中
        xx = abs(x)
        yy = abs(y)
        t = yy
        ex = []
        while t <= xx:
            ex.append(t)
            t = t+t

        # 每次比较xx与ex[i]的大小
        # 若xx >= ex[i]说明除得动，那么res=res+2^i
        res = 0
        for i in range(len(ex)-1, -1, -1):
            if xx >= ex[i]:
                xx = xx-ex[i]
                res = res+(1 << i)

        if is_minus:
            res = -res
        if res < -(1 << 31) or res > (1 << 31)-1:
            res = (1 << 31)-1

        return res


# @lc code=end
