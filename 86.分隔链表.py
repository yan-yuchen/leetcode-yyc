#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        p_head=p=ListNode(0)
        q_head=q=ListNode(0)

        cur=head

        while cur:
            if cur.val<x:
                p.next=cur
                p=p.next

            if cur.val>=x:
                q.next=cur
                q=q.next

            cur=cur.next

        q.next=None
        p.next=q_head.next

        return p_head.next
# @lc code=end

