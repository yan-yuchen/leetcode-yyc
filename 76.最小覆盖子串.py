#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 使用哈希表来存储
        from collections import defaultdict
        window = defaultdict(int) # 哈希表维护的是[j,i]区间中各个字符出现多少次
        ht = defaultdict(int) # 哈希表维护的是t字符串各个字符出现多少次
        for char in t:
            ht[char] += 1

        res = ""
        # 滑动窗口内有效的字母个数，因为窗口内可能有些字母无效
        cnt = 0
        j = 0

        for i in range(len(s)):
            # 往滑动窗口加入当前元素
            window[s[i]] += 1

            # 假如加入当前元素后，当前元素在窗口内出现的次数没有超过要求的次数
            if window[s[i]] <= ht[s[i]]:
                cnt += 1

            # 检查 s[j]是否多余，因为s[i]有可能等于s[j], 如果是，则移除s[j]
            while j <= i and window[s[j]] > ht[s[j]]:
                window[s[j]] -= 1
                j += 1

            # 检查当前窗口已经包含了 T 中所有字符，更新答案
            if cnt == len(t):
                if res == "" or i - j + 1 < len(res):
                    res = s[j:i + 1]

        return res
   
# @lc code=end

