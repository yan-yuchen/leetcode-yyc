#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        cur=dummy
        while cur.next and cur.next.next:
            if cur.next.val==cur.next.next.val:
                t=cur.next.val
                while cur.next and cur.next.val==t:
                    cur.next=cur.next.next
            else:
                cur=cur.next

        return dummy.next

# @lc code=end

