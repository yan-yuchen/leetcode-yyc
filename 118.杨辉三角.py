#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]

        for i in range(numRows):
            row=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(res[i-1][j]+res[i-1][j-1])
            res.append(row)

        return res
# @lc code=end

