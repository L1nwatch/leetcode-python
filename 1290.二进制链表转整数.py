#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = str(head.val)
        current_node = head
        while current_node.next:
            current_node = current_node.next
            number = number + str(current_node.val)
        return int(number,2)

        
# @lc code=end

