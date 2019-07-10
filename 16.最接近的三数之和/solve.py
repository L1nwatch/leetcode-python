#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums = sorted(nums)
        length = len(nums)
        result = 2 ** 31
        for i in range(length - 2):
            l, r = i + 1, length - 1
            while l < r:
                this_sum = nums[i] + nums[l] + nums[r]
                if this_sum < target:
                    l += 1
                    while nums[l] == nums[l - 1] and (l + 1) < length:
                        l += 1
                    if abs(target - this_sum) < abs(target - result):
                        result = this_sum
                elif this_sum > target:
                    r -= 1
                    while nums[r] == nums[r + 1] and (r - 1) > i:
                        r -= 1
                    if abs(target - this_sum) < abs(target - result):
                        result = this_sum
                else:
                    return target
        return result
