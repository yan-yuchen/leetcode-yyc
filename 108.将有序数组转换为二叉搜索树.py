#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 直接获取有序数组中值作为根就可以，递归生成左子树和右子树即可
        if len(nums)==0: return
        elif len(nums)==1: return TreeNode(nums[0])
        
        mid = len(nums)//2
        node=TreeNode(nums[mid])
        node.left=self.sortedArrayToBST(nums[:mid])
        node.right=self.sortedArrayToBST(nums[mid+1:])
    
        return node
# @lc code=end

