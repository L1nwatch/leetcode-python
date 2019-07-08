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
        test_data_list = [3, 4, 9, 58, 1994]
        right_answer_list = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.intToRoman(num=test_data)
            self.assertEqual(my_answer, right_answer)


if __name__ == "__main__":
    pass
