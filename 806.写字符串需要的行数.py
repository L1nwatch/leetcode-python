#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        answer = [1,0]
        for char in s:
            width = widths[ord(char)-ord('a')]
            if answer[1] + width <= 100:
                answer[1] += width
            else:
                answer[0] += 1
                answer[1] = width
        return answer
# @lc code=end

