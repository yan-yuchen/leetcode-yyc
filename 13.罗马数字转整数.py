#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(len(s)):
            if (i < len(s)-1):
                # 比较前后两个字符，如果后大于等于前如‘VIII’则直接加
                # 如果后小于前如‘IV’，则需要减
                s1, s2 = s[i], s[i+1]
                if (a[s1] >= a[s2]):
                    res = res+a[s1]
                else:
                    res = res-a[s1]

            else:
                res = res+a[s[i]]

        return res

        # @lc code=end
