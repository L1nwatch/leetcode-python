# @before-stub-for-debug-begin
from python3problem83 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while slow.next is not None:
            if slow.val == fast.val:
                slow.next, fast = fast.next, fast.next
            else:
                slow, fast = fast, fast.next
        return head
# @lc code=end
