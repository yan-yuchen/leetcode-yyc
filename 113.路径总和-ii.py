#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        path=[]
        res=[]

        def dfs(root,sum,path):
            if not root:
                return
            if not root.left and not root.right:
                if sum == root.val:
                    path=path+[root.val]
                    res.append(path)
            dfs(root.left,sum-root.val,path+[root.val])
            dfs(root.right,sum-root.val,path+[root.val])

        dfs(root,targetSum,path)
        
        return res
# @lc code=end

