#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 鏈�闀垮洖鏂囧瓙涓?
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        # i表示中心， 枚举每个回文字符中心
        # 由左右两个指针l，r分别左右移动
        for i in range(len(s)):

            # 回文字符为奇数
            l, r = i-1, i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l = l-1
                r = r+1
            # 更新res
            if (r-l-1 > len(res)):
                res = s[l+1:r]

            # 回文字符为偶数
            l, r = i, i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l = l-1
                r = r+1
            if (r-l-1 > len(res)):
                res = s[l+1:r]

        return res

# @lc code=end
