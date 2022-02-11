#
# @lc app=leetcode.cn id=1854 lang=python3
#
# [1854] 人口最多的年份
#

# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = dict()
        for birth,death in logs:
            for i in range(birth,death):
                count[i] = count.get(i,0)+1
        
        answer = max_value = 0
        for year,value in count.items():
            if value > max_value:
                answer = year
                max_value = value
            elif value == max_value:
                answer = min(answer,year)
        return answer
# @lc code=end

