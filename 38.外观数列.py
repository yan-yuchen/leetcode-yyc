#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:

        s = '1'
        for _ in range(n-1):
            # 双指针
            start = 0
            end = 0
            t = ''
            while(end < len(s)):
                while end < len(s) and s[start] == s[end]:
                    end = end+1
                t = t+str(end-start)+s[start]
                start = end

            s = t

        return s


# @lc code=end
