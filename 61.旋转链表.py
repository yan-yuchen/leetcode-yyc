#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return 
        
        temp=head
        n=1
        # 计算链表长度
        while temp.next:
            temp=temp.next
            n=n+1

        k=k%n #实际需要从后往前移多少次
        temp.next=head # 形成闭合环状链表

        # 寻找移动后头节点位置
        for i in range(n-k):
            temp=temp.next

        head=temp.next
        temp.next=None # 断开环状链表

        return head
        
# @lc code=end

