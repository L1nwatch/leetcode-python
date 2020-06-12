#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
"""
import unittest
from solve import Solution, ListNode

__author__ = '__L1n__w@tch'


class TestSolution(unittest.TestCase):
    def test_solve_func(self):
        test_data_list = [
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))),
            ListNode(1, ListNode(2, ListNode(3, None))),
            ListNode(1, ListNode(2, None)),
            ListNode(1, None),
            None
        ]
        right_answer_data = [
            ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5, None))))),
            ListNode(2, ListNode(1, ListNode(4, ListNode(3, None)))),
            ListNode(2, ListNode(1, ListNode(3, None))),
            ListNode(2, ListNode(1, None)),
            ListNode(1, None),
            None
        ]

        s = Solution()
        for each_test_data, each_right_answer in zip(test_data_list, right_answer_data):
            my_answer = s.swapPairs(head=each_test_data)
            right_answer = each_right_answer
            right_answer_list = list()
            while right_answer is not None:
                right_answer_list.append(right_answer.val)
                right_answer = right_answer.next
            my_answer_list = list()
            while my_answer is not None:
                my_answer_list.append(my_answer.val)
                my_answer = my_answer.next
            print("[*] 测试数据：{}".format(my_answer_list))
            self.assertEqual(right_answer_list, my_answer_list, "测试用例：{}".format(right_answer_list))


if __name__ == "__main__":
    pass
