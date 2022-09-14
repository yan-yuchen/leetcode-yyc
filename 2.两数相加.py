#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 涓ゆ暟鐩稿姞
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 模拟竖式加法，取出链表中每一位的数值，相加后放入新的链表中即可，需要注意进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化第三个输出链表
        # 这里ListNode是class需要初始化，之后赋值的时候同理
        dummy = ListNode(0)
        node = dummy

        node_1 = l1
        node_2 = l2
        carry = 0  # 进位

        while (node_1 or node_2 or carry):

            num_1 = 0
            num_2 = 0

            if node_1:
                num_1 = node_1.val  # 提取当前节点的值
                node_1 = node_1.next  # 前进到下一个节点
            if node_2:
                num_2 = node_2.val
                node_2 = node_2.next

            if (num_1+num_2+carry > 9):  # 需要进位的时候
                res = num_1+num_2+carry-10
                node.next = ListNode(res)  # 新初始化一个节点，然后连接到node上
                carry = 1
            else:
                res = num_1+num_2+carry
                node.next = ListNode(res)
                carry = 0

            node = node.next  # 前进到下一个节点

        return dummy.next  # 一定要返回初始链表头
# @lc code=end
