#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 在链表的操作中，添加一个哑节点(dummy),让它的指针指向链表的头节点

# 好处：
    # 省略头节点为空时的情况的判断；
    # 头节点和其他节点进行同样的操作时，由于头节点没有前一个节点，需要对这种情况进行单独判断，但加入虚拟节点以后，头节点就可以当作普通节点看待。
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums=[]
        # 放到一个数组里排序
        for l in lists:
            node=l
            while node:
                nums.append(node.val)
                node=node.next

        nums.sort()

        # 放到一个链表里
        dummy=ListNode(0)
        head=dummy
        for i in range(len(nums)):
            head.next=ListNode(nums[i])
            # 等价于，先创建节点，再连接
            # tmp=ListNode()
            # tmp.val=nums[i]
            # head.next=tmp
            head=head.next

        return dummy.next

# @lc code=end

