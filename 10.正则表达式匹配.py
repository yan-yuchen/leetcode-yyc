#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
# 状态表示：f[i][j] s字符的前i个元素, p 字符的前j个元素
# 状态计算: p[j + 1]是一般字符  f[i + 1][j + 1] = f[i][j]  if s[i + 1] == p[j + 1]
#           p[j] 是 "."  f[i + 1][j + 1] = f[i][j]
#           p[j] 是 "*"
#                   1. p[j] != s[i + 1]  f[i + 1][j + 1] = f[i][j - 1]  # 删除一个
#                   2. p[j] == s[i + 1] or p[j] == "."
#                       f[i + 1][j + 1] = f[i + 1][j]      # 一个
#                       f[i + 1][j + 1] = f[i][j + 1]      # 多个
#                       f[i + 1][j + 1] = f[j + 1][j - 1]  # 空

class Solution(object):
    def isMatch(self, s, p):
        sn, pn = len(s), len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True

        for i in range(pn):
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(sn):
            for j in range(pn):
                # 精准匹配，所以取决于s的前i个字符和p的前j个字符是否匹配。dp[i+1][j+1] = dp[i][j]
                if s[i] == p[j]:
                    dp[i + 1][j + 1] = dp[i][j]

                # .可以代表任何字符，所和上面一种情况一样
                if p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]

                if p[j] == "*":
                    # 如果不能匹配，那么*只能代表0个字符，这时候取决于s的前i个字符和p的前j - 1个字符是否匹配。
                    if p[j - 1] != s[i] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    # 如果能匹配有3种可能的情况，需要对这三种情况取或：
                    else:
                        dp[i + 1][j + 1] = dp[i +
                                              1][j] or dp[i][j + 1] or dp[i + 1][j - 1]

        return dp[sn][pn]

# @lc code=end
