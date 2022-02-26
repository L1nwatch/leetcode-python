#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
"""
import unittest
from solve import Solution

__author__ = '__L1n__w@tch'


class TestSolution(unittest.TestCase):
    def get_right_answer(self, n: int, k: int) -> list:
        from itertools import combinations
        a = list(combinations(list(range(1, n + 1)), k))
        return [list(x) for x in a]

    def test_solve_func(self):
        test_data_list = [
            [4, 2],
            [1, 1],
        ]

        s = Solution()
        for each_test_data in test_data_list:
            my_answer = s.combine(*each_test_data)
            right_answer = self.get_right_answer(*each_test_data)

            self.assertEqual(len(right_answer), len(my_answer), f"长度不匹配：期望{len(right_answer)} != 实际{len(my_answer)}")

            for each_right_answer in right_answer:
                self.assertIn(each_right_answer, my_answer, f"缺失:{each_right_answer}")


if __name__ == "__main__":
    pass
