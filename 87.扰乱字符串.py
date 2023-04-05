#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    @functools.lru_cache(None) 
    # 可以把函数的输入和输出结果缓存住，在后续调用中如果遇到了相同的输入，直接从缓存里面读
    # 递归
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)==0:
            return True
        if len(s1)==1:
            return s1==s2
        if sorted(s1)!=sorted(s2):
            return False
        
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        
        return False
    
# @lc code=end

