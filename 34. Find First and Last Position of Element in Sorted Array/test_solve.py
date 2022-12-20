#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

__author__ = '__L1n__w@tch'

import unittest
from solve import Solution


class TestSolution(unittest.TestCase):
    def test_solve_func(self):
        test_data = ([5, 7, 7, 8, 8, 10], 8)
        right_answer = [3, 4]
        my_answer = Solution().searchRange(*test_data)
        self.assertEqual(right_answer, my_answer)

    def test_solve_func2(self):
        test_data = ([5, 7, 7, 8, 8, 10], 6)
        right_answer = [-1, -1]
        my_answer = Solution().searchRange(*test_data)
        self.assertEqual(right_answer, my_answer)

    def test_solve_func3(self):
        test_data = ([], 0)
        right_answer = [-1, -1]
        my_answer = Solution().searchRange(*test_data)
        self.assertEqual(right_answer, my_answer)


if __name__ == "__main__":
    pass
