#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        st=[False]*10
        res=''

        for i in range(n):  # 枚举每一个位置
            fact=1

            # 计算出剩余的选法: (n-i)!
            for j in range(1,n-i):
                fact=fact*j

            # 遍历所有数字
            for j in range(1,n+1):
                if st[j]:  # 没有用过的数字
                    continue
                if fact<k: #如果没有到k说明第i位不是j，继续做阶乘
                    k=k-fact
                else:  # 若剩余的数不够，那么当前的数就是要选的
                    res=res+str(j)
                    st[j]=True
                    break

        return res            

# @lc code=end

