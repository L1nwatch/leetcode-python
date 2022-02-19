#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        current_node = head
        while current_node:
            current_node = current_node.next
            count += 1
        
        middle = count // 2
        current_node = head
        while middle > 0:
            current_node = current_node.next
            middle -= 1
        return current_node
# @lc code=end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        current_node = head
        while current_node is not None:
            length += 1
            current_node = current_node.next

        answer_node = head
        middle = length // 2 + 1
        for i in range(1, middle):
            answer_node = answer_node.next
        return answer_node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow