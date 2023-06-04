#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path=[] # 记录每一条支路的总和
        
        def dfs(root,sum):
            if not root:
                return
            sum=sum+root.val

            if not root.left and not root.right: # 如果是叶子节点才将总和放到list里面
                path.append(sum)

            dfs(root.left,sum)
            dfs(root.right,sum)

        dfs(root,0)

        if targetSum in path:
            return True
        else:
            return False
# @lc code=end

