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

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        substring = set()
        answer = 0
        right = -1
        for i in range(length):
            if i != 0:
                substring.remove(s[i-1])
            while right + 1 < length and s[right+1] not in substring:
                substring.add(s[right+1])
                right += 1
            answer = max(answer, right - i + 1)
        return answer