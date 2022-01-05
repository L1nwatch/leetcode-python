#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        import collections
        counter = collections.Counter(arr)
        answer = set()
        for key, value in counter.items():
            if key == value:
                answer.add(key)
        if len(answer) == 0:
            return -1
        else:
            return max(answer)
# @lc code=end
