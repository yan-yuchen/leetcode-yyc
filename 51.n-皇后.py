#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        col = [False]*n  # 记录每一个使用过的列
        dg = [False]*(2*n)  # 记录对角线
        udg = [False]*(2*n)  # 记录反方向对角线
        path = [['.']*n for _ in range(n)]

        def dfs(j):
            if j == n:
                res.append(["".join(path[i]) for i in range(n)])

            # 一行一行搜索，需要同时满足这列，对角线与反方向对角线没有使用过
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
