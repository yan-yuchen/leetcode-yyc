#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        i=0
        carry=0
        res=''

        while i<len(a) or i <len(b) or carry:
            if i<len(a):
                carry=carry+int(a[i])
            if i < len(b):
                carry=carry+int(b[i])

            res=res+str(carry%2)
            carry=carry//2
            i=i+1

        return res[::-1]

# @lc code=end

