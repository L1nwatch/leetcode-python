#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer = 0
        arr_length = len(arr)
        import itertools
        odd_num = (arr_length+1)//2
        for length in range(odd_num):
            length = 2 * length + 1
            for i in range(arr_length-length+1):
                #print(arr[i:i+length])
                answer += sum(arr[i:i+length])
        return answer

# @lc code=end
