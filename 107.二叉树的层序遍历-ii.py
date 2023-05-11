#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 层序遍历后倒序输出即可
        if root == None:
            return []
         
        queue=[root]
        res=[]

        while queue:
            res.append([node.val for node in queue])
            temp=[]

            for node in queue:
                if node.left:
                   temp.append(node.left)
                if node.right:
                     temp.append(node.right)

            queue=temp

        return res[::-1]
# @lc code=end

