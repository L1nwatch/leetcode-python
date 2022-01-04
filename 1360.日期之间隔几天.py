#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        date1 = datetime.datetime.strptime(date1,"%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2,"%Y-%m-%d")
        return abs((date2-date1).days)
# @lc code=end

