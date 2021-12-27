#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_number = -1
        for index in range(len(arr)-1, -1, -1):
            arr[index], max_number = max_number, max(arr[index], max_number)
        return arr
# @lc code=end
