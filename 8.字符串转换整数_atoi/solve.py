#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import string

__author__ = '__L1n__w@tch'


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip(" ")
        result = ""
        # with "-" or "+"
        if str.startswith("-") or str.startswith("+"):
            result += str[0]
            str = str[1:]
        for each_num in str:
            if each_num in string.digits:
                result += each_num
            else:
                break
        num = result.lstrip("-+")
        if len(num) <= 0 or num[0] not in string.digits:
            return 0
        result = int(result)
        if abs(result) > (2 ** 31 - 1):
            return -2 ** 31 if result < 0 else (2 ** 31 - 1)
        return result
