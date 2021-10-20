#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        set_a = set()
        node = headA
        while node:
            set_a.add(node)
            node = node.next
        node = headB
        while node:
            if node in set_a:
                return node
            node = node.next
        return None
        
# @lc code=end

