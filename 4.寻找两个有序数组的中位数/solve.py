#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""

__author__ = '__L1n__w@tch'


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        length = len(s)
        if length <= 1:
            return s
        dp = [[False for l in range(length)] for r in range(length)]
        max_length = 0
        result = s[0]
        for r in range(1, length):
            for l in range(r):
                if s[l] == s[r] and ((r - l) == 1 or (r - l) == 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if (r - l + 1) > max_length:
                        max_length = r - l + 1
                        result = s[l:r + 1]
        return result


class Solution1:
    def is_huiwen(self, string):
        return string == string[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_s = ""
        for i in range(len(s)):
            temp_s = ""
            temp_max = ""
            for j in range(i, len(s)):
                temp_s += s[j]
                if self.is_huiwen(temp_s) and len(temp_s) > len(temp_max):
                    temp_max = temp_s
            if len(temp_max) > len(max_s):
                max_s = temp_max
        return max_s
