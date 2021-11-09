#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new_score = sorted(score, reverse=True)
        result = list()
        for each_data in score:
            index = new_score.index(each_data)
            if index == 0:
                result.append("Gold Medal")
            elif index == 1:
                result.append("Silver Medal")
            elif index == 2:
                result.append("Bronze Medal")
            else:
                result.append(f"{index+1}")
        return result
# @lc code=end
