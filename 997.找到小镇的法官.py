#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return n

        people_set = set(list(range(1, n+1)))
        counter = dict()
        for x, y in trust:
            if x in people_set:
                people_set.remove(x)
            if len(people_set) == 0:
                return -1
            counter[y] = counter.get(y, 0)+1
        if len(people_set) >= 2:
            return -1
        answer = people_set.pop()
        if counter[answer] == n-1:
            return answer
        return -1
# @lc code=end
