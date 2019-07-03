#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""

__author__ = '__L1n__w@tch'


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x.startswith("-"):
            answer = int(x[1:][::-1]) * -1
        else:
            answer = int(x[::-1])
        if abs(answer) > (2 ** 31 - 1):
            return 0
        return answer
