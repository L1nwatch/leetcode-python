#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""

__author__ = '__L1n__w@tch'

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            this_set = set()
            for j in range(i,len(s)):
                if s[j] not in this_set:
                    this_set.add(s[j])
                else:
                    break
            max_length = len(this_set) if len(this_set) > max_length else max_length
        return max_length
