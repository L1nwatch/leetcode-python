#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        for i in range(0, len(nums)):
            if nums[i] in window_set:
                return True
            window_set.add(nums[i])
            if len(window_set) > k:
                window_set.remove(nums[i-k])
        return False

# @lc code=end
