#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def get_char(self, num: int) -> str:
        return chr(ord('a')+num-1)

    def freqAlphabets(self, s: str) -> str:
        answer = str()
        index = len(s)-1
        while index >= 0:
            if s[index] == "#":
                answer += self.get_char(int(s[index-2:index]))
                index -= 3
            else:
                answer += self.get_char(int(s[index]))
                index -= 1
        return answer[::-1]


# @lc code=end
