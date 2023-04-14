#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]

        def dfs(start,temp):
            if len(temp)>4:
                return 
            if start==len(s) and len(temp)==4:
                return res.append('.'.join(temp))

            for i in range(start,len(s)):
                if int(s[start:i+1])>255 or (s[start]=='0' and len(s[start:i+1])>=2):# 取出来的大于255，或者不是单个0，那么不满足要求
                    return
                temp.append(s[start:i+1])
                dfs(i+1,temp)
                temp.pop()

        dfs(0,[])

        return res
# @lc code=end

