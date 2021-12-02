#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        if n == 1:
            return 0
        answer = 0
        n = bin(n)[2:]

        left, right = 0, 1
        while right < len(n):
            if n[right] == "0":
                right += 1
            else:
                answer = max(answer, right-left)
                left = right
                right += 1
        return answer
# @lc code=end
