#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""

__author__ = '__L1n__w@tch'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 得到第一个数
        num1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            num1 += str(l1.val)

        # 得到第二个数
        num2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            num2 += str(l2.val)

        num1 = num1[::-1]
        num2 = num2[::-1]
        # 相加，返回结果
        result = str(int(num1) + int(num2))
        result = result[::-1]
        root_list = ListNode(int(result[0]), None)
        last_list = root_list
        for i in range(1, len(result)):
            last_list.next = ListNode(int(result[i]), None)
            last_list = last_list.next
        return root_list
