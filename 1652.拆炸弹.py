#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k == 0:
            return [0]*len(code)
        if k > 0:
            answer = list()
            for i in range(1, length+1):
                part_sum = 0
                for j in range(k):
                    part_sum += code[(i+j) % length]
                answer.append(part_sum)
            return answer
        if k < 0:
            answer = list()
            for i in range(length):
                part_sum = 0
                for j in range(k, 0):
                    part_sum += code[(i+j) % length]
                answer.append(part_sum)
            return answer

# @lc code=end
