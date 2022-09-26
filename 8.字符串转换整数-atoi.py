#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 瀛楃涓茶浆鎹㈡暣鏁? (atoi)
#

# @lc code=start

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        str = s.lstrip()  # 清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')  # 设置正则规则
        #  ^表示在行的开头匹配，保证以+-0-9开头；后续只能是连续数字。
        num = num_re.findall(str)  # 查找匹配的内容

        # ^[\+\-]?\d+
        # ^ 表示匹配字符串开头，我们匹配的就是 '+'  '-'  号
        # [] 表示匹配包含的任一字符，比如[0-9]就是匹配数字字符 0 - 9 中的一个
        # ? 表示前面一个字符出现零次或者一次，这里用 ? 是因为 '+' 号可以省略
        # \d 表示一个数字 0 - 9 范围
        # + 表示前面一个字符出现一次或者多次，\d+ 合一起就能匹配一连串数字了

        # 无法将list中元素直接转换为int，所以需要先解包
        num = int(*num)  # 由于返回的是个列表，解包并且转换成整数

        return max(min(num, INT_MAX), INT_MIN)  # 返回值
# @lc code=end
