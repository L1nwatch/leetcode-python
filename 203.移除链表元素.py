#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if head:
            pre = head
            current_node = head.next
            while current_node:
                if current_node.val == val:
                    pre.next = current_node.next
                else:
                    pre = current_node
                current_node = current_node.next
        return head

# @lc code=end

