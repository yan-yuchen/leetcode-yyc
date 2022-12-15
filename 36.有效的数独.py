#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 判断行
        for i in range(9):
            store = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in store:
                    return False
                else:
                    store.append(board[i][j])

        # 判断列
        for j in range(9):
            store = []
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in store:
                    return False
                else:
                    store.append(board[i][j])

        # 判断九宫格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                store = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y] == '.':
                            continue
                        if board[x][y] in store:
                            return False
                        else:
                            store.append(board[x][y])

        return True
# @lc code=end
