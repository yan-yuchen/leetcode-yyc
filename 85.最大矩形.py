#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 思路：先使用前缀和求出每一行每个位置连续1的个数
        # 之后参考84题的方法，用单调栈求出最大矩阵面积
        if not matrix:
            return 0
        
        m,n=len(matrix),len(matrix[0])
        pre=[0]*(n+1)
        res=0

        for i in range(m):
            # 前缀和
            for j in range(n):
                if matrix[i][j]=='1':
                    pre[j]=pre[j]+1
                else:
                    pre[j]=0

            # 单调栈
            stack=[-1]
            for k,num in enumerate(pre):
                while stack and pre[stack[-1]]>num:
                    index=stack.pop()
                    res=max(res,pre[index]*(k-stack[-1]-1))
                stack.append(k)

        return res

# @lc code=end

