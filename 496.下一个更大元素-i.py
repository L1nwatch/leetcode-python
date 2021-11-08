#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        for each_num in nums1:
            find = False
            for each_num2 in nums2[nums2.index(each_num):]:
                if each_num2 > each_num:
                    result.append(each_num2)
                    find = True
                    break
            if not find:
                result.append(-1)
        return result
# @lc code=end

