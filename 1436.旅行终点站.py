#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        counter = dict()
        for start, end in paths:
            counter[start] = counter.get(start, 0)+1
            counter[end] = counter.get(end, 0)-1
        for city, count in counter.items():
            if count == -1:
                return city

# @lc code=end
