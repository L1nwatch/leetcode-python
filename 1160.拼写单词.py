#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer = 0
        from collections import Counter
        counter = Counter(chars)
        for word in words:
            import copy
            temp_count = copy.deepcopy(counter)
            for char in word:
                if temp_count.get(char, 0) > 0:
                    temp_count[char] -= 1
                else:
                    break
            else:
                answer += len(word)
        return answer
# @lc code=end
