#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        candidates.sort()

        def dfs(num, target):
            if target < 0:
                return

            if target == 0:
                t = path[:]
                res.append(t)
                return

            for i in range(num, len(candidates)):

                # 去重，避免多次出现[1,7],[1,7]这样的重复，出现是因为存在多个1
                # [1,1,6]的情况是i<num，也就是仍在第一次遇到1搜多的时候
                # i > num且candidates[i] == candidates[i-1]说明已经是第二次搜索时遇到1，跳过即可去重
                if i > num and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])

                dfs(i+1, target-candidates[i])

                path.pop()

        dfs(0, target)
        return res

# @lc code=end
