#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res=[]

        for i in range(rowIndex+1):
            row=[]
            for j in range(0,i+1):
                if j==0 or i==j:
                    row.append(1)
                else:
                    row.append(res[i-1][j]+res[i-1][j-1])
            res.append(row)
        
        return res[rowIndex]
# @lc code=end

