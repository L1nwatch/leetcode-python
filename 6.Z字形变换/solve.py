#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""

__author__ = '__L1n__w@tch'


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        list_nums = min(numRows, len(s))
        result = [list() for i in range(list_nums)]
        go_down = True
        x = 0
        for each_char in s:
            if go_down:
                # down
                result[x].append(each_char)
                x += 1
            else:
                # right-top
                result[x].append(each_char)
                x -= 1
            # last_line
            if x == numRows:
                go_down = False  # right_top
                x -= 2
            # first_line
            if x == 0:
                go_down= True
        result_str = ""
        for each_list in result:
            result_str += "".join(each_list)
        return result_str
