#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0

        n = len(s)
        m = len(p)
        s = ' '+s
        p = ' '+p

        # 建立next数组，存储字符串的最长相同的前缀和后缀
        next = [0]*(m+1)
        # i表示当前子串最后一个元素
        # 通过j的移动，判断p[i],p[j+1]是否相等来确定最长相等前后缀
        j = 0
        for i in range(2, m+1):
            while j and p[i] != p[j+1]:
                # 如果 p[i] 与 p[j+1]不相同，也就是遇到 前后缀末尾不相同的情况，就要向前回溯。
                # next[j]就是记录着j（包括j）之前的子串的相同前后缀的长度。
                # 那么 p[i] 与 p[j+1] 不相同，就要找 j+1前一个元素在next数组里的值（就是next[j]）
                j = next[j]
            if p[i] == p[j+1]:
                # 相等则j+1
                j = j+1
                next[i] = j

        # kmp 字符串匹配
        j = 0
        for i in range(1, n+1):
            while j and s[i] != p[j+1]:
                j = next[j]
            if s[i] == p[j+1]:
                j = j+1
            if j == m:
                return i-m

        return -1


# @lc code=end
