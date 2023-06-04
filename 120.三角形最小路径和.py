#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # 由下向上计算
        triangle=triangle[::-1]

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j]=triangle[i][j]+min(triangle[i-1][j],triangle[i-1][j+1])

        return triangle[-1][-1]
# @lc code=end

