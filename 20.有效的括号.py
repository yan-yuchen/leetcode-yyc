#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    # 使用栈来维护
    # 左括号，直接入栈，如果右括号，看和栈顶的左括号是否匹配，不匹配直接返回false，否则弹出；最后返回栈 == 空
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
