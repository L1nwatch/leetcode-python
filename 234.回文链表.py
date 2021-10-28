#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = [head.val]
        right = head
        while right.next:
            right = right.next
            nums.append(right.val)
        return nums == nums[::-1]
        
# @lc code=end

