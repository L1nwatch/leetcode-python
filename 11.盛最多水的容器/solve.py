#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    # https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode/
    def maxArea(self, height: list) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


class Solution_Timeout:
    def maxArea(self, height: list) -> int:
        max_result = 0
        length = len(height)
        for i in range(length):
            for j in range(length - 1, i, -1):
                this_result = (j - i) * min(height[i], height[j])
                max_result = max(this_result, max_result)
        return max_result
