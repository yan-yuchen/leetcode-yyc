#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # 主对角线翻转
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 水平翻转
        for k in range(len(matrix)):
            i, j = 0, len(matrix)-1

            while i < j:
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
                i = i+1
                j = j-1


# @lc code=end
