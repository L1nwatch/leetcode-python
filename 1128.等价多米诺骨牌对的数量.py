#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        nums = [0] * 100
        answer = 0
        for x, y in dominoes:
            value = (x*10+y if x >= y else y*10+x)
            answer += nums[value]
            nums[value] += 1
        return answer
# @lc code=end
        from itertools import combinations
        answer = 0
        for each in combinations(dominoes, 2):
            domino1 = each[0]
            domino2 = each[1]
            if (domino1[0] == domino2[0] and domino1[1] == domino2[1]) or (domino1[0] == domino2[1] and domino1[1] == domino2[0]):
                answer += 1
        return answer
