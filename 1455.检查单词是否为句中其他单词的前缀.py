#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index,word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return index + 1
        else:
            return -1
# @lc code=end

