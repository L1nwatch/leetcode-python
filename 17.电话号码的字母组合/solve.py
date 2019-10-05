#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re
from itertools import permutations

__author__ = '__L1n__w@tch'


class Solution:
    def letterCombinations(self, digits: str) -> list:
        letters_digit_map = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) <= 0:
            return digits

        result = list()
        i = 0
        for each_char in letters_digit_map[digits[i]]:
            result.append("{}".format(each_char))
        i += 1

        while i < len(digits):
            temp_result = list()
            for each_result in result:
                for each_char in letters_digit_map[digits[i]]:
                    temp_result.append("{}{}".format(each_result, each_char))
            result = temp_result
            i += 1

        return result
