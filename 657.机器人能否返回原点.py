#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        answer = [0, 0]
        for each_char in moves:
            if each_char == "L":
                answer[0] += 1
            elif each_char == "R":
                answer[0] -= 1
            elif each_char == "U":
                answer[1] += 1
            elif each_char == "D":
                answer[1] -= 1
        return answer[0] == 0 and answer[1] == 0
# @lc code=end
