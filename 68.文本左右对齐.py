#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        # 这里不能用for i in range(len(words)), 因为循环末尾i要重置到j - 1，再i += 1
        while i < len(words):
            # 看一下当前行可以放哪些单词，从下一个单词开始看
            j = i + 1
            # length当前单词的长度
            length = len(words[i])
            # 当j没有越界，并且当前单词长度加上空格，加上下一个单词长度没有超过maxWidth时，j+=1
            while j < len(words) and length + 1 + len(words[j]) <= maxWidth:
                length += 1 + len(words[j])
                j += 1
            # 循环结束后，得到可以放在当前行的单词为 words[i] ~ words[j - 1]
            line = ''
            # 第一种情况： 左对齐
            # j == len(words)说明在最后一行，或者j = i + 1: 这一行只放一个单词words[i]
            if j == len(words) or j == i + 1:
                # 先把word[i] 添进这一行
                line += words[i]
                # 再加上空格和word[i + 1] ～ word[j - 1]
                for k in range(i + 1, j):
                    line += ' ' + words[k]
                # 不足最大长度，补上空格
                while len(line) < maxWidth:
                    line += ' '
            else:
                # 第二种情况： 左右对齐
                # cnt 空隙的数量, 单词数量为 j - i, 空隙数量少一个再减去1
                cnt = j - i - 1
                # r：有多少个剩余空格可用， length（是单词总长度以及空隙个数的空格），再加上空隙个数的空格
                r = maxWidth - length + cnt
                # 加上当前单词
                line += words[i]
                # 从第0个空隙开始
                k = 0
                # 先看空格较多的空隙
                while k < r % cnt:
                    line += ' ' * (r // cnt + 1) + words[i + k + 1]
                    k += 1
                # 空格较少空隙：
                while k < cnt:
                    line += ' ' * (r // cnt) + words[i + k + 1]
                    k += 1

            # 把当前行加进答案
            res.append(line)
            # i ~ j - 1单词已经加入，i从j开始
            i = j

        return res

# @lc code=end

