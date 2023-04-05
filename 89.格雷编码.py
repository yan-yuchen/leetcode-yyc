#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n==1:
            return [0,1]
        
        # 为得到第n个格雷编码，则需要将第n-1个编码作反转操作
        left=self.grayCode(n-1)
        right=left.copy() # 镜面对称
        right.reverse() # 反转
        right=[x+(1<<(n-1)) for x in right] #反转后首位补1

        return left+right
# @lc code=end

