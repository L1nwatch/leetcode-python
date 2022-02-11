#
# @lc app=leetcode.cn id=1832 lang=python3
#
# [1832] 判断句子是否为全字母句
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        import string
        for char in string.ascii_lowercase:
            if char not in sentence:
                return False
        return True
# @lc code=end

