#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        left, right = None, head
        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        return left
# @lc code=end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        answer_list = list()
        while head:
            answer_list.append(head)
            head = head.next
        for i in range(len(answer_list)-1,-1,-1):
            if i > 0:
                answer_list[i].next = answer_list[i-1]
            else:
                answer_list[i].next = None
        return answer_list[-1] if len(answer_list) > 0 else None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = [None]
        current_node = head
        while current_node:
            stack.append(current_node)
            current_node.next,current_node = stack[-2],current_node.next
        return stack[-1]
