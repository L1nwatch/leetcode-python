#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        min_num, first_positive_num = 0, len(nums)-1
        while nums[first_positive_num] >= 0 and min_num <= first_positive_num:
            first_positive_num -= 1
        if first_positive_num != len(nums) - 1:
            first_positive_num += 1
        negative_numbers = first_positive_num-min_num
        if negative_numbers >= k:
            while k > 0:
                nums[min_num] = -nums[min_num]
                min_num += 1
                k -= 1
        else:
            while negative_numbers > 0:
                negative_numbers -= 1
                nums[min_num] = - nums[min_num]
                min_num += 1
                k -= 1
            min_num -= 1
            if k % 2 == 1:
                if abs(nums[first_positive_num]) >= abs(nums[min_num]):
                    nums[min_num] = -nums[min_num]
                else:
                    nums[first_positive_num] = -nums[first_positive_num]
        return sum(nums)


# @lc code=end
