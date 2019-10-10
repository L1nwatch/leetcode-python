#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re
from typing import List

__author__ = '__L1n__w@tch'


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return [""]
        answer = list()
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    answer.append("({}){}".format(left, right))
        return answer
