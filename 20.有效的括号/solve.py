#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for each_char in s:
            if each_char in ("(", "{", "["):
                stack.append(each_char)
            elif each_char in (")", "}", "]"):
                if len(stack) <= 0:
                    return False
                this_char = stack.pop(-1)
                if (each_char == ")" and this_char != "(") or (each_char == "}" and this_char != "{") or (
                        each_char == "]" and this_char != "["):
                    return False
        return True if len(stack) == 0 else False
