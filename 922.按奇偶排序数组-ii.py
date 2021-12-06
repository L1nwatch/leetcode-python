#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_list, even_list = list(), list()
        for num in nums:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)

        answer = list()
        for x, y in zip(even_list, odd_list):
            answer.append(x)
            answer.append(y)
        return answer

# @lc code=end
