#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        answer = (sum(salary) - salary[0]-salary[-1])/(len(salary)-2)
        return answer

# @lc code=end
