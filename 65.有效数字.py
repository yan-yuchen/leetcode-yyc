#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        numbers=[str(i) for i in range(10)]
        n=len(s)
        num_show,e_show,dot_show,num_e_after=False,False,False,False
        for i in range(n):
            c=s[i]
            if c in numbers:
                num_show=True
                num_e_after=True
            elif c in ('+','-'):
                # +—号只能出现在开头或者e后面
                if i>0 and s[i-1]!='e' and s[i-1]!='E':
                    return False
            elif c == 'e' or c =='E':
                # e不能出现两次，e前面要有数字，e后面也要有数字
                if e_show or not num_show:
                    return False
                e_show=True
                num_e_after=False
            elif c=='.':
                # .不能出现两次，也不能和e同时出现
                if e_show or dot_show:
                    return False
                dot_show=True
            else:
                # 出现其他字符直接false
                return False

        # 必须有数字并且e后要有数字
        return num_show and num_e_after
# @lc code=end

