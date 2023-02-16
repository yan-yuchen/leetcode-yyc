#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        k=0
        res=[]

        while k<len(intervals) and intervals[k][1]<newInterval[0]:
            res.append(intervals[k])
            k=k+1

        if k<len(intervals):
            newInterval[0]=min(newInterval[0],intervals[k][0])
            while k<len(intervals) and intervals[k][0]<=newInterval[1]:
                newInterval[1]=max(newInterval[1],intervals[k][1])
                k=k+1

        res.append(newInterval)

        while k<len(intervals):
            res.append(intervals[k])
            k=k+1
        
        return res

# @lc code=end

