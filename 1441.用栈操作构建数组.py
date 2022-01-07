#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = list()
        length_target = len(target)
        index = 0
        for i in range(1, n+1):
            answer.append("Push")
            if i != target[index]:
                answer.append("Pop")
            else:
                index += 1
            if index >= length_target:
                break
        return answer
# @lc code=end
