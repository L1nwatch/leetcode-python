#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    def romanToInt(self, s: str) -> int:
        this_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result = 0
        s = list(s)
        while len(s) > 0:
            this_num = s.pop(0)
            if this_num in ("I", "X", "C") and len(s) > 0:
                if this_num == "I" and s[0] in ("V","X"):
                    this_num += s.pop(0)
                if this_num == "X" and s[0] in ("L","C"):
                    this_num += s.pop(0)
                if this_num == "C" and s[0] in ("D", "M"):
                    this_num += s.pop(0)
            result += this_map[this_num]
        return result
