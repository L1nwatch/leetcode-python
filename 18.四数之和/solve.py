#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re
from typing import List

__author__ = '__L1n__w@tch'


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1
                while c != d:
                    this_list = (nums[a], nums[b], nums[c], nums[d])
                    sum_this_list = sum(this_list)
                    if sum_this_list == target:
                        result.add(this_list)
                        c += 1
                    elif sum_this_list > target:
                        d -= 1
                    elif sum_this_list < target:
                        c += 1
        return list([list(i) for i in result])
