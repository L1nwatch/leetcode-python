#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

__author__ = '__L1n__w@tch'


class ListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = low = fast = head
        if fast and fast.next:
            fast = fast.next_node
        while fast:
            if low.value == fast.value:
                fast = fast.next_node
                low.next_node = fast
            else:
                low = low.next_node
                fast = fast.next_node
        return root


if __name__ == "__main__":
    pass
