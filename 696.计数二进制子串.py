#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        index, answer, length, last_count = 0, 0, len(s), 0
        while index < length:
            char = s[index]
            count = 0
            while index < length and s[index] == char:
                count += 1
                index += 1
            answer += min(last_count, count)
            last_count = count
        return answer
# @lc code=end
