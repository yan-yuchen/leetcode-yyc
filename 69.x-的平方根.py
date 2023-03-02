#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=1,x

        if x==0:
            return 0
        if x==1:
            return 1

        while left<right:
            mid = (left+right+1)//2
            if mid *mid <=x:
                left=mid
            else:
                right=mid-1

        return left
# @lc code=end

