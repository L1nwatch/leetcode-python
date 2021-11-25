#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = dict()
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                count[char] = count.get(char, 0) + 1

        min_length = 1001
        min_word = None
        for word in words:
            import collections
            count_word = collections.Counter(word)
            if all([count[char] <= count_word.get(char, 0) for char in count.keys()]):
                if len(word) < min_length:
                    min_length = len(word)
                    min_word = word
        return min_word
# @lc code=end
