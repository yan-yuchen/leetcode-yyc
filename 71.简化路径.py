#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        for p in path.split('/'):
            if p == '..':
                # 如果是'..'要返回上级目录
                if stack:
                    stack.pop()
            else:
                # 如果不是'..'
                # 是'.'的话就是当前目录本身，不需要加入stack
                if p and p != '.':
                    stack.append(p)

        return '/'+'/'.join(stack)
# @lc code=end

