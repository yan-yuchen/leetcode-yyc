#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子�?
#

# @lc code=start

# 滑动窗口法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        w = []  # 滑动窗口
        max_length = 0

        # 遍历字符串
        for c in s:
            # 如果字符不在滑动窗口中，将此字符串加入窗口
            if c not in w:
                w.append(c)

            # 如果字符串在窗口中已经存在
            else:
                # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
                w[:] = w[w.index(c)+1:]
                # 将当前字符加入窗口
                w.append(c)

            max_length = max(len(w), max_length)

        return max_length



# @lc code=end
