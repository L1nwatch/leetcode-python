#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(p,s):
            return True
        return False
