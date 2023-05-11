#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res=True
        self.dfs(root)
        return self.res

    def dfs(self,root):
        if not root:
            return 0
        lh=self.dfs(root.left)
        rh=self.dfs(root.right)
        if abs(lh-rh) > 1:
            self.res=False
        
        return max(lh,rh)+1
         
# @lc code=end

