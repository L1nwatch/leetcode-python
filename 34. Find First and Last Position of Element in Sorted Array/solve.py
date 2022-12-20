#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

__author__ = '__L1n__w@tch'


class Solution:
    def binary_search(self, nums, target, need_lower) -> int:
        low, high = 0, len(nums) - 1
        answer = len(nums)
        while low <= high:
            middle = low + (high - low) // 2
            value = nums[middle]
            if value > target or (value >= target and need_lower):
                high = middle - 1
                answer = middle
            else:
                low = middle + 1

        return answer

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]
        start = self.binary_search(nums, target, True)
        end = self.binary_search(nums, target, False) - 1
        if start <= end and end < len(nums) and nums[start] == nums[end] == target:
            result = [start, end]
        return result


if __name__ == "__main__":
    pass
