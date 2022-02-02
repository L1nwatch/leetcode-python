#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        source_nums = sorted(nums)
        length = len(nums)
        for x in range(min(100,length)):
            for i in range(length):
                if nums[i] != source_nums[(i+x)%length]:
                    break
            else:
                return True
        return False
# @lc code=end

