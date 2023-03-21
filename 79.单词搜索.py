#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board,word,step,x,y):
            if board[x][y]!=word[step]:
                return False
            
            if step==len(word)-1:
                return True
            
            dirs = [[-1,0],[0,1], [1,0],[0,-1]]
            temp  = board[x][y]
            board[x][y] = '.'

            for dx, dy in dirs:
                new_x = dx + x 
                new_y = dy + y 
                if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]) or board[new_x][new_y] == '.':
                    continue
                if dfs(board, word, step + 1, new_x, new_y):
                    return True
                
            board[x][y] = temp

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, 0, i, j):
                    return True
                
        return False

# @lc code=end

