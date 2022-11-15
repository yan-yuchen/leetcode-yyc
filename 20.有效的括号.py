#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, string: str) -> bool:
        dic = {']': '[',
               ')': '(',
               '}': '{'}
        stack = []

        for s in string:
            if stack and s in dic:
                if stack[-1] == dic[s]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s)

        if len(stack) == 0:
            return True
        else:
            return False
# @lc code=end
