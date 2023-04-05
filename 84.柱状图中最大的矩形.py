#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=[0]*(n+1),[0]*(n+1)

        # 我们栈中元素存储的是下标，而对于两端的柱子，它们两侧的边界分别为-1和n。
        # 先从左往右循环，找到每个元素左边第一个比它矮的元素，并放入left数组。再从右往左循环，找到右边第一个比它矮的元素，并放入right数组
        st=[]
        for i in range(n):
            while len(st) and heights[st[-1]]>=heights[i]: # 维护一个单调递增的栈，元素如果比栈顶元素小则弹出栈顶元素，反复执行
                st.pop()
            if not len(st): # 栈为空则直接为左边界
                l[i]=-1
            else: # 不为空则此时栈顶元素即离heights[i]左边最近的小于它的值
                l[i]=st[-1]
            st.append(i)

        st=[]
        for i in range(n-1,-1,-1):
            while len(st) and heights[st[-1]]>=heights[i]:
                st.pop()
            if not len(st):
                r[i]=n
            else:
                r[i]=st[-1]
            st.append(i)

        res=0
        for i in range(n):
            res=max(res,heights[i]*(r[i]-l[i]-1))

        return res
            

# @lc code=end

