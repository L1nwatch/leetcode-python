#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        current_node = root
        result = list()
        slack = list()
        while current_node or len(slack) > 0:
            while current_node:
                slack.append(current_node)
                result.append(current_node.val)
                current_node = current_node.left
            current_node = slack.pop()
            current_node = current_node.right
        return result
# @lc code=end

