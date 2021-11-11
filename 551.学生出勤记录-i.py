#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        series_p_times = 0
        a_times = 0
        for each_status in s:
            if each_status != "L":
                series_p_times = 0
            if each_status == "A":
                a_times += 1
                if a_times >= 2:
                    return False
            elif each_status == "L":
                series_p_times += 1
                if series_p_times >= 3:
                    return False
        return True

# @lc code=end

