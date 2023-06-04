#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth=[]

        # dfs所有深度，最后返回最小的即可
        def dfs(node,d):
            if not node.left and not node.right:
                depth.append(d)
                return

            d=d+1

            if node.left:
                dfs(node.left,d)
            if node.right:
                dfs(node.right,d)

        dfs(root,1)

        return min(depth)

            

# @lc code=end

