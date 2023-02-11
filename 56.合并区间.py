#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        # 根据第一个元素排序
        intervals.sort(key=lambda x: x[0])

        for x in intervals:
            if len(res) == 0:
                res.append(x)
            else:
                # 如果res中最后一个集合的右元素大于x的左元素，则说明存在重叠关系
                if res[-1][1] >= x[0]:
                    res[-1][1] = max(res[-1][1], x[1])
                else:
                    res.append(x)

        return res
        # @lc code=end
