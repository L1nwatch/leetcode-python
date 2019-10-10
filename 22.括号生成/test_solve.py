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
        test_data_list = [3]
        right_answer_list = [["((()))", "(()())", "(())()", "()(())", "()()()"]]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.generateParenthesis(n=test_data)
            self.assertEqual(right_answer, my_answer, "测试用例：{}".format(test_data))


if __name__ == "__main__":
    pass
