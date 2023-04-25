#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        root_list=[]
        # 得到当前树中序遍历得到的列表 
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            root_list.append(root)
            dfs(root.right)

        dfs(root)

        # 得到正确的二叉搜索树应有的有序列表 (二叉搜索树中序遍历的结果应该是单调的)
        root_order=sorted(root_list, key=lambda x: x.val)

        # 比较这两个列表得到交换的两个节点 (值不对应的两个节点)
        p,q=[root_list[i] for i in range(len(root_list)) if root_list[i]!=root_order[i]]

        # 重置两个节点的值
        p.val, q.val = q.val, p.val
# @lc code=end

