#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        # 每一个小列表按排序后相等放一起
        for s in strs:
            t = ''.join(sorted(s))
            if t in res:
                res[t].append(s)
            else:
                res[t] = [s]

        return list(res.values())

# @lc code=end
