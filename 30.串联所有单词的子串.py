#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        slen = len(s)
        wlen = len(words[0])
        llen = len(words)

        count = collections.Counter(words)
        # 利用collections.Counter生成对words的哈希表
        # L = ['red', 'blue', 'red', 'green', 'blue', 'blue']
        # Counter(L)
        # Counter({'red': 2, 'blue': 3, 'green': 1}

        res = []
        for i in range(slen):  # 一位一位遍历起始位置

            # 创建一个哈希表用于判断滑动窗口中的字符是否满足串联子串的条件
            # 出现次数相等即满足串联子串要求，故与words的哈希表完全相等则满足
            diff = collections.Counter()

            if i+wlen*llen > slen:
                break
            else:
                # 开始滑动窗口，由于单词的长度还有总数量都是已知的，所以在滑动的时，每次增加的长度都是wlen
                for j in range(i, i+wlen*llen, wlen):
                    newwords = s[j:j+wlen]
                    diff[newwords] = diff[newwords]+1

            # 哈希表相等则说明符合要求
            if diff == count:
                res.append(i)

        return res

# @lc code=end
