#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 非叶结点都有两个孩子，左右孩子必定相邻，所以左孩子的 next 指针应当指向右孩子
        # 右孩子的 next 指针应当指向 父节点 next 所指结点 的左孩子（如 Figure B 所示，结点5的next应当指向 其父节点2 的 next 指针所指结点3 的左孩子）

        if root:
            if root.left:
                root.left.next=root.right
                if root.next:
                    root.right.next=root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root
        
# @lc code=end

