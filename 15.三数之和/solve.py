#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    def threeSum(self, nums: list) -> list:

        nums = sorted(nums)
        length = len(nums)
        result_list = list()
        if length > 0 and nums[0] <= 0:
            for i in range(length - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                l, r = i + 1, length - 1
                while l < r:
                    this_sum = nums[i] + nums[l] + nums[r]
                    if this_sum < 0:
                        l += 1
                        while nums[l] == nums[l - 1] and (l + 1) < length:
                            l += 1
                    elif this_sum > 0:
                        r -= 1
                        while nums[r] == nums[r + 1] and (r - 1) > i:
                            r -= 1
                    else:
                        result_list.append((nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and (l + 1) < length:
                            l += 1
                        while nums[r] == nums[r + 1] and (r - 1) > i:
                            r -= 1
        return result_list

    def threeSum_timeout(self, nums: list) -> list:
        # Time-out
        nums = sorted(nums)
        length = len(nums)
        result_list = list()
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if j == i or k == i or j == k:
                        continue
                    this_sum = sum([nums[i], nums[j], nums[k]])
                    if this_sum == 0:
                        if (nums[i], nums[j], nums[k]) not in result_list:
                            result_list.append((nums[i], nums[j], nums[k]))
                    elif this_sum > 0:
                        break
        return list(set(result_list))
