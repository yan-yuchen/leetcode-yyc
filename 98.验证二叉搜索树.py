#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_val, max_val):
            if not node:  # 边界条件，如果node为空肯定是二叉搜索树
                return True
            if not min_val < node.val < max_val:  # 如果当前节点超出上下界范围，肯定不是
                return False
            # 走到下面这步说明已经满足了如题所述的二叉搜索树的前两个条件
            # 那么只需要递归判断当前节点的左右子树是否同时是二叉搜索树即可
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf')) # 对于根节点，它的上下限为无穷大和无穷小

# @lc code=end

