#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        answer = (releaseTimes[0], keysPressed[0])
        for i in range(1, len(releaseTimes)):
            press_time = releaseTimes[i]-releaseTimes[i-1]
            answer = max(answer, (press_time, keysPressed[i]))
        return answer[1]
# @lc code=end
