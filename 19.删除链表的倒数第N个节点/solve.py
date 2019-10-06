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
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_map, i = {1: head}, 1
        cur_node = head
        while cur_node.next != None:
            i += 1
            node_map[i] = cur_node.next
            cur_node = cur_node.next

        # 删除第一个节点
        if i == n:
            head = node_map[2] if i >= 2 else None
        # 删除最后一个节点
        elif n == 1:
            node_map[i - n].next = None
        # 删除中间一个节点
        else:
            node_map[i - n].next = node_map[i - n + 2]

        return head
