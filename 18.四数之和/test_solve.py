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
        test_data_list = [([1, 0, -1, 0, -2, 2], 0), ([0, 0, 0, 0], 0), ([-3, -2, -1, 0, 0, 1, 2, 3], 0)]
        right_answer_list = [[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], [[0, 0, 0, 0]],
                             [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3],
                              [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.fourSum(nums=test_data[0], target=test_data[1])
            self.assertEqual(right_answer, my_answer)


if __name__ == "__main__":
    pass
