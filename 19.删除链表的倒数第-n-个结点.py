#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针做法：i，j保持一个n的距离，当i移动到结尾时，j刚好到达倒数第n个节点
        dummy = ListNode(next=head)
        i = dummy
        j = dummy
        count = 0

        while(i):
            i = i.next
            count = count+1
            if count > n+1:
                j = j.next

        j.next = j.next.next

        return dummy.next


# @lc code=end
