#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = list()
        index = 0
        length = len(nums)
        while index < length:
            start = nums[index]
            index += 1
            while index < length and nums[index] - 1 == nums[index-1]:
                index += 1
            end = nums[index-1]
            result.append(str(start) if start ==
                          end else "{}->{}".format(start, end))

        return result
# @lc code=end
        result = list()
        if len(nums) <= 0:
            return result
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i-1]:
                result.append(str(start) if start ==
                              end else "{}->{}".format(start, end))
                start = nums[i]
            end = nums[i]
        if start == end:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, end))

        return result
