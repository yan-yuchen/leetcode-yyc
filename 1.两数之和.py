#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 涓ゆ暟涔嬪拰
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 两层循环效率较低，采用哈希表优化
        # 每次循环将数据放入哈希表中，判断target-num是否在哈希表中即可
        hashmap = {}  # 字典
        for index, item in enumerate(nums):     # enumerate能同时列举索引和数值
            if (target-item in hashmap):        # 如果target-item在hashmap中，
                return hashmap[target-item], index    # 则返回target-item与item的索引
            # 将数值存储到hashmap中（字典形式{item1:index1 ,item2:index2, ...}）
            hashmap[item] = index

# @lc code=end
