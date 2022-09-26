#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 瀛楀舰鍙樻崲
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        res = [""]*(numRows)  # 生成['', '', '', '']，每一个‘’存储当行的数据
        flag = -1  # 当遇到第一行与最后一行flag改变
        i = 0  # 表示行

        if (numRows < 2):
            return s

        # 模拟z字过程，先从上到下再从下到上，当遇到第一行与最后一行时，i反向，即flag取反
        # 结果放到res中，n个字符串，每个字符串分别存储一行的字符
        for c in s:
            res[i] = res[i]+c

            if (i == 0 or i == numRows-1):
                flag = -flag

            i = i+flag*1

        return "".join(res)

        # @lc code=end
