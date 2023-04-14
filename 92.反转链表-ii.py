#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(left-1):
            pre=pre.next

        cur=pre.next

        # 头插法
        for i in range(right-left):
            temp1=cur.next
            temp2=temp1.next

            cur.next=temp2
            temp1.next=pre.next
            pre.next=temp1

        return dummy.next
# @lc code=end

