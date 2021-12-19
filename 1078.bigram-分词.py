#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        answer = list()
        count = 0
        index = 0
        while index < len(words):
            if count == 2:
                answer.append(words[index])
                index -= 1
                count = 0

            if count == 0 and words[index] == first:
                count = 1
            elif count == 1 and words[index] == second:
                count = 2
            elif count == 1 and words[index] == first:
                count = 1
            else:
                count = 0
            index += 1
        return answer
            

# @lc code=end

