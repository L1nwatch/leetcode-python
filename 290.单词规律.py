#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = dict()
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern[i] not in hash_map:
                if words[i] in hash_map.values():
                    return False
                hash_map[pattern[i]] = words[i]
                continue
            if hash_map[pattern[i]] != words[i]:
                return False
        return True
# @lc code=end
