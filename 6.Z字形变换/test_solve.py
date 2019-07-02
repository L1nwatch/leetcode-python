#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
"""
import unittest
from solve import Solution

__author__ = '__L1n__w@tch'


class TestSolution(unittest.TestCase):
    def test_solve_func(self):
        test_data_list = [("LEETCODEISHIRING", 3), ("LEETCODEISHIRING", 4), ("ABC", 1),("ABCDEF",2)]
        right_answer_list = ["LCIRETOESIIGEDHN", "LDREOEIIECIHNTSG","ABC","ACEBDF"]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.convert(s=test_data[0], numRows=test_data[1])
            self.assertEqual(my_answer, right_answer)


if __name__ == "__main__":
    pass
