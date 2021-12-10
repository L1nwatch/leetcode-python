#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer = 0
        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                if strs[i][j] > strs[i+1][j]:
                    answer += 1
                    break
        return answer
# @lc code=end

