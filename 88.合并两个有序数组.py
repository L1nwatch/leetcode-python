#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result_list = list()
        left, right = 0, 0
        while left <= m-1 and right <= n-1:
            if nums1[left] < nums2[right]:
                result_list.append(nums1[left])
                left += 1
            elif nums1[left] == nums2[right]:
                result_list.append(nums1[left])
                left += 1
            elif nums1[left] > nums2[right]:
                result_list.append(nums2[right])
                right += 1
        while left <= m-1:
            result_list.append(nums1[left])
            left += 1
        while right <= n-1:
            result_list.append(nums2[right])
            right += 1
        for i in range(m+n):
            nums1[i] = result_list[i]

# @lc code=end
