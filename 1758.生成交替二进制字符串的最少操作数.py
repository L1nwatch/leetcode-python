#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def get_answer(self,s,first_char):
        pre = int(first_char)
        answer = 0
        for char in s[1:]:
            char = int(char)
            if char ^ pre == 1:
                pre = char
            else:
                pre = char ^ 1
                answer += 1
        return answer

    def minOperations(self, s: str) -> int:
        answer1 = self.get_answer(s,s[0])
        answer2 = self.get_answer(s,int(s[0])^1)+1       
        return min(answer1,answer2)

# @lc code=end

