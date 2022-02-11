#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        answer = [""]*10
        for temp_word in s.split(" "):
            index=int(temp_word[-1])
            word=temp_word[:-1]
            answer[index] = word
        return " ".join([x for x in answer if x != ""])
# @lc code=end

