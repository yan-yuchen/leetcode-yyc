#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        path = []

        def dfs(step):
            # 每轮的终止条件
            if step == len(digits):
                if path:
                    res.append(''.join(path))
                return  # 本次dfs结束，运行至path.pop()

            # dfs
            for ch in dic[digits[step]]:
                path.append(ch)
                dfs(step+1)   # 递归调用，继续选择下一位数字所对应的字母
                path.pop()    # 回溯

        dfs(0)
        return res

        # @lc code=end
