#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""

"""
import re
from typing import List

__author__ = '__L1n__w@tch'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None
        if next:
            self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l_point, r_point, temp_point = head, head.next, head
        while r_point:
            l_point.next = r_point.next
            r_point.next = l_point
            if l_point == head:
                head = r_point
                temp_point = l_point
            else:
                temp_point.next = r_point
                temp_point = l_point
            if not l_point.next:
                break
            l_point = l_point.next
            r_point = l_point.next

        return head
