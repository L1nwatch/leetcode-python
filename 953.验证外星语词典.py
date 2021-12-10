#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def is_asc(self, word1: str, word2: str) -> bool:
        for i in range(min(len(word1), len(word2))):
            order_1, order_2 = self.order[word1[i]], self.order[word2[i]]
            if order_1 > order_2:
                return False
            elif order_1 < order_2:
                return True
        if len(word1) > len(word2):
            return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.order = dict(zip(order, [x for x in range(len(order))]))

        answer = True
        for i in range(len(words)-1):
            if not self.is_asc(words[i], words[i+1]):
                answer = False
        return answer

# @lc code=end
