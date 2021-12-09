#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = list()
        numbers = list([x for x in range(len(s)+1)])
        for char in s:
            if char == "I":
                answer.append(numbers.pop(0))
            else:
                answer.append(numbers.pop())
        answer.extend(numbers)
        return answer
# @lc code=end

