#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        answer = set()
        nums = str()
        for char in word:
            if char.isdigit():
                nums += char
            else:
                if nums != "":
                    answer.add(int(nums))
                nums = str()
        else:
            if nums != "":
                answer.add(int(nums))
        return len(answer)
# @lc code=end

