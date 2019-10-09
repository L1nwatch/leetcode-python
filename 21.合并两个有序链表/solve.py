#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re

__author__ = '__L1n__w@tch'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head_result = None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val >= l2.val:
                result = head_result = l2
                l2 = l2.next
            else:
                result = head_result = l1
                l1 = l1.next
        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next
            result = result.next
        if l1 is not None:
            result.next = l1
        if l2 is not None:
            result.next = l2
        return head_result
