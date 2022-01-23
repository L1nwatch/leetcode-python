#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                answer += 1
        return answer
# @lc code=end

