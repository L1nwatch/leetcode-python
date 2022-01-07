#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                answer += 1
        return answer
# @lc code=end
