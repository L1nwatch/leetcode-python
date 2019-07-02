#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""

__author__ = '__L1n__w@tch'


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        length = len(nums1)
        if length % 2 == 0:
            return (nums1[length // 2] + nums1[(length - 1) // 2]) / 2.0
        else:
            return float(nums1[length // 2])
