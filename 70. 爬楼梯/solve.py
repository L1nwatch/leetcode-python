#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re
from typing import List

__author__ = '__L1n__w@tch'


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, b + a
        return b
