#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):

            # 边界条件
            if y == 9:
                x = x+1
                y = 0

            # 结束
            if x == 9:
                return True

            # 已经有数字了则进行下一个
            if board[x][y] != '.':
                return dfs(x, y+1)

            # 开始dfs
            for ch in "123456789":
                if (ch not in row[x]) and (ch not in col[y]) and (ch not in cell[x//3][y//3]):

                    board[x][y] = ch
                    row[x].append(board[x][y])
                    col[y].append(board[x][y])
                    cell[x//3][y//3].append(board[x][y])

                    if(dfs(x, y+1)):
                        return True

                    # 回溯，恢复现场
                    board[x][y] = '.'
                    row[x].remove(ch)
                    col[y].remove(ch)
                    cell[x//3][y//3].remove(ch)

            return False

        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        cell = [[[] for _ in range(3)] for _ in range(3)]

        # 对已有数字处理
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    cell[i//3][j//3].append(board[i][j])

        dfs(0, 0)


# @lc code=end
