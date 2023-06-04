#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # 思路：每一层拿出来放到queue里，然后两两连接即可
        if not root:
            return root
        
        # pairwise:从对象中获取连续的重叠对
        # 比如说：s= ‘abcde’，itertools.pairwise(s)的输出应该为，ab, bc, cd, de;
        
        queue=[root]

        while queue:
            temp=queue
            queue=[]

            for x,y in pairwise(temp):
                x.next=y

            for node in temp:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
        
# @lc code=end

