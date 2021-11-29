#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = list()
        start, end = 0, 0
        length = len(s)
        while end < length:
            if s[end] == s[start]:
                end += 1
                if end == length and end-start >= 3:
                    answer.append([start, end-1])
            elif end - start >= 3:
                answer.append([start, end - 1])
                start = end
                end += 1
            else:
                start = end
                end += 1
                

        return answer
# @lc code=end
