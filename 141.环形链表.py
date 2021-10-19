#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        node_set = set()
        current_node = head
        while current_node not in node_set:
            node_set.add(current_node)
            current_node = current_node.next
            if current_node is None:
                return False
        return True
# @lc code=end

