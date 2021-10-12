#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result_list = list()
        stack = list()
        node = root
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result_list.append(node.val)
            node = node.right
        return result_list

# @lc code=end
        result_list = list()
        if root:
            if root.left:
                left_list = self.inorderTraversal(root.left)
                result_list = left_list + result_list
            if root.val != 0:
                result_list.append(root.val)
            if root.right:
                right_list = self.inorderTraversal(root.right)
                result_list.extend(right_list)
        return result_list