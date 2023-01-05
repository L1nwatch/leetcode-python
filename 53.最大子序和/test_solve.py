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
        test_data = ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8])
        right_answer = (6, 1, 23)

        s = Solution()
        for test_input, answer in zip(test_data, right_answer):
            my_answer = s.maxSubArray(nums=test_input)
            self.assertEqual(my_answer, answer)


if __name__ == "__main__":
    pass
