#
# @lc app=leetcode.cn id=1791 lang=python3
#
# [1791] 找出星型图的中心节点
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = dict()
        for u,v in edges:
            counter[u] = counter.get(u,0)+1
            counter[v] = counter.get(v,0)+1
        max_value = max(counter.values())
        for key,value in counter.items():
            if value == max_value:
                return key
# @lc code=end

