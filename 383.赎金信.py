#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        count = collections.Counter(ransomNote)
        for each_char in magazine:
            if each_char in count:
                count[each_char] -= 1
                if count[each_char] == 0:
                    count.pop(each_char)
        return len(count) == 0
# @lc code=end

