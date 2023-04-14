#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res,stack=[],[]

        while root or stack:
            # 先遍历左子树
            while root:
                stack.append(root)
                root=root.left
            # 到头了，返回上一级
            root=stack.pop()
            res.append(root.val)
            # 遍历右子树
            root=root.right

        return res
# @lc code=end

