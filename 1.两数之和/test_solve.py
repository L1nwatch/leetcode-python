#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import unittest
from solve import Solution

__author__ = '__L1n__w@tch'


class TestSolution(unittest.TestCase):
    def test_solve_func(self):
        test_data_list = [([2, 7, 11, 15], 9), ([2, 11, 7], 9)]
        right_answer_list = [[0, 1], [0, 2]]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            self.assertEqual(s.twoSum(nums=test_data[0], target=test_data[1]), right_answer)


if __name__ == "__main__":
    pass
