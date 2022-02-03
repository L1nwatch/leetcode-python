#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = str()
        length_word1 = len(word1)
        length_word2 = len(word2)
        for i in range(min(length_word1,length_word2)):
            answer += word1[i]
            answer += word2[i]
        else:
            answer += word1[i+1:]
            answer += word2[i+1:]
        return answer
# @lc code=end

