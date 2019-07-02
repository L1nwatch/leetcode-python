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
        test_data_list = [([1,3],[2]),([1,2],[3,4])]
        right_answer_list = [2.0, 2.5]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.findMedianSortedArrays(nums1=test_data[0],nums2=test_data[1])
            self.assertEqual(my_answer, right_answer)



if __name__ == "__main__":
    pass
