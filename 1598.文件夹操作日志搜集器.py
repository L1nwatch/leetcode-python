#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answer = 0
        for log in logs:
            if log == "../":
                answer = max(0, answer - 1)
            elif log == "./":
                pass
            else:
                answer += 1
        return answer

# @lc code=end
