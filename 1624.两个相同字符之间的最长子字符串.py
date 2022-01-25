#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        answer = -1
        length = len(s)
        for i in range(length):
            left = i
            right = length-1

            if answer > right-left:
                break

            while left < right:
                if s[left] == s[right]:
                    answer = max(answer, right-left-1)
                    break
                else:
                    right -= 1
        return answer

# @lc code=end
