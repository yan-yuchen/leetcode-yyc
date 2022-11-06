#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # 法一 使用zip
        # res = ''
        # # 函数调用时，可以用*或者**解包可迭代对象，作为参数传递。
        # # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        # for s in list(zip(*strs)):
        #     # 在zip里的for循环打印出s是这样的
        #     # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        #     # set用于去重，若去重后长度等于1则意味着是公共前缀
        #     if len(set(s)) == 1:
        #         res = res+s[0]
        #     else:
        #         break

        # return res

        # 法二 暴力做法
        # 找出最短与最长的字符串，比较两者的最长公共前缀即可
        res = ''
        if len(strs) == 0:
            return ''

        s1, s2 = min(strs), max(strs)

        for i in range(len(s1)):
            if (s1[i] == s2[i]):
                res = res+s1[i]
            else:
                break

        return res

# @lc code=end
