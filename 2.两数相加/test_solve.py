#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
"""
import unittest
from solve import Solution

__author__ = '__L1n__w@tch'


class TestSolution(unittest.TestCase):
    class ListNode:
        def __init__(self, x, next):
            self.val = x
            self.next = next

    def test_solve_func(self):
        test_data_list = [(self.ListNode(2, self.ListNode(4, self.ListNode(3, None))),
                           self.ListNode(5, self.ListNode(6, self.ListNode(4, None)))),
                          (self.ListNode(1, None), self.ListNode(2, None))]
        right_answer_list = [self.ListNode(7, self.ListNode(0, self.ListNode(8, None))), self.ListNode(3, None)]

        for test_data, right_answer in zip(test_data_list, right_answer_list):
            s = Solution()
            my_answer = s.addTwoNumbers(l1=test_data[0], l2=test_data[1])
            self.assertEqual(my_answer.val,right_answer.val)
            while my_answer.next:
                my_answer = my_answer.next
                right_answer = right_answer.next
                self.assertEqual(my_answer.val,right_answer.val)


if __name__ == "__main__":
    pass
