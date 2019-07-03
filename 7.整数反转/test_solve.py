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
        test_data_list = [123, -123, 120, 1534236469]
        right_answer_list = [321, -321, 21, 0]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.reverse(x=test_data)
            self.assertEqual(my_answer, right_answer)


if __name__ == "__main__":
    pass
