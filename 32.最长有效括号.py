#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0

        for i in range(len(s)):
            # 如果是（则把i进栈
            if s[i] == '(':
                stack.append(i)
            else:
                # 如果是）则代表左括号匹配到了有括号，弹出栈顶元素
                stack.pop()
                # 弹出后判断当前栈
                if not stack:
                    # 若栈为空，表示之前的所有的 ( 匹配成功，上一步出栈的是栈底的-1或者是前一个不匹配的 ) 。则更新栈底为当前 ) 的索引，表示不匹配的位置
                    stack.append(i)
                else:
                    # 如果当前栈是空的表示匹配结束，i-栈顶元素 即为有效匹配的长度
                    res = max(res, i-stack[-1])

        return res

# @lc code=end
