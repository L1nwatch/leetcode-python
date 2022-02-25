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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        index1,index2 = 0,0
        if list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list1.val <= list2.val:
            head = current_node = list1
            list1 = list1.next
        else:
            head = current_node = list2
            list2 = list2.next
        
        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next
        while list1:
            current_node.next = list1
            current_node = current_node.next
            list1 = list1.next
        while list2:
            current_node.next = list2
            current_node = current_node.next
            list2 = list2.next
        return head