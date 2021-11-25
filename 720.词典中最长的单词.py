#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)
        words = sorted(words, key=lambda c: (-len(c), c))
        for word in words:
            if all([word[:i] in words_set for i in range(1, len(word))]):
                return word
        return ""
# @lc code=end
