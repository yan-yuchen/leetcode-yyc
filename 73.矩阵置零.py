#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        m_set=set()
        n_set=set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    m_set.add(i)
                    n_set.add(j)

        for i in range(m):
            for j in range(n):
                if i in m_set or j in n_set:
                    matrix[i][j]=0

        return matrix
# @lc code=end

