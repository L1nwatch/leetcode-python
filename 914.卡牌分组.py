#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        import collections
        counter = collections.Counter(deck)
        min_num = min(counter.values())
        if min_num < 2:
            return False

        for x in range(2, min_num+1):
            answer = True
            for each_value in counter.values():
                if each_value % x != 0:
                    answer = False
                    break
            if answer:
                return answer

        return False
# @lc code=end
