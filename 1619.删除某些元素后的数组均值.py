#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length = len(arr)
        arr.sort()
        left = length // 20
        right = length - length // 20
        answer = sum(arr[left:right])/(right-left)
        return answer
# @lc code=end
