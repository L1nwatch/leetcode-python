#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        answer = list()
        for i, word in enumerate(sentence.split(" ")):
            if word[0].lower() in ("a", "e", "i", "o", "u"):
                answer.append(word + "ma" + "a"*(i+1))
            else:
                answer.append(word[1:] + word[0] + "ma" + "a"*(i+1))
        return " ".join(answer)
# @lc code=end
