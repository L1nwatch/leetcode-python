#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hash_set = set()
        import collections
        deque = collections.deque()
        deque.append(root)
        while deque:
            current_node = deque.popleft()
            if k-current_node.val in hash_set:
                return True
            hash_set.add(current_node.val)
            if current_node.left:
                deque.append(current_node.left)
            if current_node.right:
                deque.append(current_node.right)
        return False
# @lc code=end

