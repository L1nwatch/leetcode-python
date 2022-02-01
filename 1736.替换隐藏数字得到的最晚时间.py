#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        hour,minute = time.split(":")
        if hour == "??":
            hour = "23"
        elif hour[0] == "?":
            if '4' <= hour[1] <= '9':
                hour = f"1{hour[1]}"
            else:
                hour = f"2{hour[1]}"
        elif hour[1] == "?":
            if '0' <= hour[0] <= '1':
                hour = f"{hour[0]}9"
            else:
                hour = f"{hour[0]}3"
        
        if minute == "??":
            minute = "59"
        elif minute[0] == "?":
            minute = f"5{minute[1]}"
        elif minute[1] == "?":
            minute = f"{minute[0]}9"
        return f"{hour}:{minute}"

# @lc code=end

