#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_num, min_num_2nd = None,None

        import collections
        deque = collections.deque()
        if root:
            deque.append(root)
            min_num = root.val
        while deque:
            current_node = deque.popleft()
            if current_node.val > min_num:
                if min_num_2nd:
                    min_num_2nd = min(current_node.val,min_num_2nd)
                else:
                    min_num_2nd = current_node.val
            if current_node.left:
                deque.append(current_node.left)
            if current_node.right:
                deque.append(current_node.right)
        return min_num_2nd if min_num_2nd else -1
# @lc code=end
