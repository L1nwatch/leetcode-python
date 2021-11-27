#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = dict()
        banned = set(banned)
        split_strings = set([",", "!", " ", ";", ".", "'", "?"])
        word = str()
        for char in paragraph+'.':
            if char in split_strings:
                word = word.lower()
                if word not in banned and word != "":
                    count[word] = count.get(word, 0) + 1
                word = str()
            else:
                word += char

        max_time, max_word = 0, None
        for word, time in count.items():
            if time > max_time:
                max_time = time
                max_word = word
        return max_word

# @lc code=end
