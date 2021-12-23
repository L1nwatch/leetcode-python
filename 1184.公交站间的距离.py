#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(
            [start, destination]), max([start, destination])
        distance_1 = sum(distance[start:destination])
        distance_2 = sum(distance[:start]) + sum(distance[destination:])
        return min([distance_1, distance_2])

# @lc code=end
