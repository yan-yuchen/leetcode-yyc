#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(l,r):
            if l>r:
                return [None]
            
            res=[]

            for i in range(l,r+1):
                left=dfs(l,i-1)
                right=dfs(i+1,r)

                for l_child in left:
                    for r_child in right:
                        root=TreeNode(i)
                        root.left=l_child
                        root.right=r_child
                        res.append(root)

            return res
        
        return dfs(1,n)
# @lc code=end

