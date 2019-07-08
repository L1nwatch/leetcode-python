#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        result = str()
        if len(strs) <= 0:
            return result
        length_list = [len(x) for x in strs]
        min_length = min(length_list)
        index = length_list.index(min_length)
        this_str = strs[index]
        for i,each_char in enumerate(this_str):
            for each_str in strs:
                if each_char != each_str[i]:
                    return result
            result += each_char
        return result