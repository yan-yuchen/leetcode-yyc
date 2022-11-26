#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        while p:
            # 第一步 判断剩余节点是否小于k个 如果小于就不用再反转了
            q = p
            for i in range(k):
                if not q:
                    break
                q = q.next
            if not q:
                break

            # 反转内部这k个节点
            a = p.next
            b = a.next
            for i in range(k-1):
                next = b.next
                b.next = a
                a = b
                b = next

            # 将反转的节点与原链表接起来
            c = p.next
            c.next = b
            p.next = a
            # p移动到下一个k个要翻转的节点处
            p = c

        return dummy.next

# @lc code=end
