#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        def dfs(num, target):
            if target < 0:
                return
            if target == 0:
                # python中list是浅拷贝，如果直接res.append(path)，则res会随path而变化
                t = path.copy()
                res.append(t)
                return

            # 这里如果是for i in range(len(candidates)):，则会出现[2,2,3],[3,2,2]等等重复答案
            # 所以添加一个参数num，每次从range(num, len(candidates))，保证枚举是正向进行的
            for i in range(num, len(candidates)):
                path.append(candidates[i])
                dfs(i, target-candidates[i])  # 这里是i不是i+1是因为自身可以多次使用
                path.remove(candidates[i])

        dfs(0, target)
        return res
# @lc code=end
