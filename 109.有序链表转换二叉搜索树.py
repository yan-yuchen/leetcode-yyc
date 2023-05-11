#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        # 求链表长度
        p,n=head,0
        while p:
            p=p.next
            n=n+1

        if n == 1: return TreeNode(head.val)

        # 得到中点
        cur=head
        for _ in range(n//2-1):
            cur=cur.next

        # 建立二叉树
        root=TreeNode(cur.next.val)

        root.right=self.sortedListToBST(cur.next.next)
        cur.next=None
        root.left=self.sortedListToBST(head)

        return root
        
# @lc code=end

