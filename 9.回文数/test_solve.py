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
        test_data_list = ["42", "   -42", "4193 with words", "words and 987", "-91283472332", "-a", "3.14159", "",
                          "0-1", "+1", "   +0 123", "2147483648"]
        right_answer_list = [42, -42, 4193, 0, -2147483648, 0, 3, 0, 0, 1, 0, 2147483647]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.myAtoi(str=test_data)
            self.assertEqual(my_answer, right_answer)


if __name__ == "__main__":
    pass
