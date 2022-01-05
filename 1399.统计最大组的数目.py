#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        answer = dict()
        for num in range(1, n+1):
            num_sum = sum([int(x) for x in list(str(num))])
            answer[num_sum] = answer.get(num_sum, 0) + 1
        max_num = max(answer.values())
        return len([x for x in answer.values() if x == max_num])
# @lc code=end
