#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        col = [False]*n
        dg = [False]*2*n
        udg = [False]*2*n
        path = [['.']*n for _ in range(n)]

        def dfs(j):
            if j == n:
                nonlocal res  # 不加这个报错local variable 'res' referenced before assignment
                res = res+1

            for i in range(n):
                if not col[i] and not dg[i+j] and not udg[i-j+n]:
                    col[i] = dg[i+j] = udg[i-j+n] = True
                    path[i][j] = 'Q'
                    dfs(j+1)
                    col[i] = dg[i+j] = udg[i-j+n] = False
                    path[i][j] = '.'

        dfs(0)
        return res


# @lc code=end
