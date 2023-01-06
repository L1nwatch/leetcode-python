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
        test_data_list = (2,3)
        right_answer_list = (2,3)

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.climbStairs(n=test_data)
            self.assertEqual(right_answer, my_answer)


if __name__ == "__main__":
    pass
