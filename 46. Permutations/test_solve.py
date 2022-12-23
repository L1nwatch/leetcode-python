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
        test_data = ([1, 2, 3], [0, 1], [1])
        right_answer = ([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], [[0, 1], [1, 0]], [[1]])
        for data, answer in zip(test_data, right_answer):
            my_answer = Solution().permute(data)
            self.assertEqual(len(my_answer), len(answer))
            for each_item in answer:
                self.assertIn(each_item, my_answer)


if __name__ == "__main__":
    pass
