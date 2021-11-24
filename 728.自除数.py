#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = list()
        for i in range(left, right+1):
            if "0" in str(i):
                continue
            if all([i % int(each_char) == 0 for each_char in str(i)]):
                answer.append(i)
        return answer
# @lc code=end
