#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        import datetime
        cur_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        begin_date = datetime.datetime(year=cur_date.year, month=1, day=1)
        return (cur_date-begin_date).days + 1
# @lc code=end
