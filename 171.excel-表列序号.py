#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        count = 0
        for each_char in columnTitle[::-1]:
            answer += (ord(each_char)-ord("A")+1)*(26**count)
            count += 1
        return answer
# @lc code=end

