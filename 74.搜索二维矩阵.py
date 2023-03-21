#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        left=0
        right=m*n-1
        
        # 二分法，将矩阵看作一维升序序列
        while left <= right:
            mid=(left+right)//2
            cur=matrix[mid//n][mid%n]

            if target==cur:
                return True
            
            if cur > target:
                right=mid-1
            else:
                left=mid+1

        return False


# @lc code=end

