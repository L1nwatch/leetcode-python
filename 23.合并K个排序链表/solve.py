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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]

        data_list = list()
        result = header = None
        for i, each_list_node in enumerate(lists):
            if each_list_node:
                data_list.append((i, each_list_node.val))
        data_list = sorted(data_list, key=lambda x: x[1])
        while len(data_list) > 0:
            low_index = data_list.pop(0)[0]
            if not header:
                result = header = lists[low_index]
            else:
                result.next = lists[low_index]
                result = result.next
            lists[low_index] = lists[low_index].next
            if lists[low_index]:
                len_data_list = len(data_list)
                for i, each_data in enumerate(data_list):
                    if lists[low_index].val <= each_data[1]:
                        data_list.insert(i, (low_index, lists[low_index].val))
                        break
                    if i == len_data_list - 1:
                        data_list.append((low_index, lists[low_index].val))
                        break
        return header


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]
        result = header = None
        while True:
            low_index = None
            data_list = list()
            flag = False
            for i, each_list_node in enumerate(lists):
                if each_list_node:
                    data_list.append((i, each_list_node.val))
                    flag = True
            data_list = sorted(data_list, key=lambda x: x[1])
            if not flag:
                break
            low_index = data_list[0][0]
            if not header:
                result = header = lists[low_index]
            else:
                result.next = lists[low_index]
                result = result.next
            lists[low_index] = lists[low_index].next
        return header


class Solution3:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]
        result = header = None
        while [True for each_node in lists if each_node].count(True) >= 1:
            low_index = None
            for i, each_list_node in enumerate(lists):
                # not empty point
                if each_list_node:
                    if low_index is None:
                        low_index = i
                        continue
                    if lists[low_index].val > each_list_node.val:
                        low_index = i
            if not header:
                result = header = lists[low_index]
            else:
                result.next = lists[low_index]
                result = result.next
            lists[low_index] = lists[low_index].next
        return header
