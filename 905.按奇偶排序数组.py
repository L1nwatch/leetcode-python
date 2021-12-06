#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = list()
        for num in nums:
            if num % 2 == 0:
                answer.insert(0,num)
            else:
                answer.append(num)
        return answer
# @lc code=end

