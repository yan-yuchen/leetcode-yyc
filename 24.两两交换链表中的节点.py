#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        p = dummy
        while p and p.next and p.next.next:
            a = p.next
            b = p.next.next

            p.next = b
            a.next = b.next
            b.next = a

            p = a

        return dummy.next
# @lc code=end
