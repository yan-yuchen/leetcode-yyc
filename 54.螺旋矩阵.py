#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n = len(matrix)
        m = len(matrix[0])
        st = [[False]*m for _ in range(n)]

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        x, y = 0, 0
        d = 0
        for i in range(n*m):
            res.append(matrix[x][y])
            st[x][y] = True
            a, b = x+dx[d], y+dy[d]

            if a < 0 or a >= n or b < 0 or b >= m or st[a][b]:
                d = (d+1) % 4
                a, b = x+dx[d], y+dy[d]

            x, y = a, b

        return res
# @lc code=end
