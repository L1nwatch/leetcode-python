#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = set()
        length = len(words)
        for i in range(length):
            print(words[i])
            if words[i] in answer:
                continue
            for j in range(i+1, length):
                if words[i] in words[j]:
                    answer.add(words[i])
                    break
                elif words[j] in words[i]:
                    answer.add(words[j])
        return list(answer)
# @lc code=end
