#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        d=0
        matrix=[[0]*n for _ in range(n)]
        st = [[False]*n for _ in range(n)]
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x,y=0,0

        for i in range(1,n*n+1):
            matrix[x][y]=i
            st[x][y]=True
            a,b=x+dx[d],y+dy[d]

            if a<0 or a>=n or b<0 or b>=n or st[a][b]:
                d=(d+1)%4
                a,b=x+dx[d],y+dy[d]

            x,y=a,b

        return matrix

# @lc code=end

