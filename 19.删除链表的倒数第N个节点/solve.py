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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        current_node = head
        while current_node:
            current_node = current_node.next
            length += 1

        if length == 1:
            return None
        if length == n:
            head = head.next
            return head

        target = length - n
        current_node = head
        for i in range(target-1):
            current_node = current_node.next
        else:
            current_node.next = current_node.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        answer = ListNode(0, head)
        slow, fast = answer, head
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return answer.next