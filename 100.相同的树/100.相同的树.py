#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        tree1, tree2 = list(), list()
        tree1_pre, tree2_pre = list(), list()
        stack = list()
        # zhong
        current_node = p
        while current_node or len(stack) > 0:
            while current_node:
                tree1_pre.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            if current_node.left is not None or current_node.right is not None:
                if current_node.left is None:
                    tree1.append(None)
            tree1.append(current_node.val)
            if current_node.left is not None or current_node.right is not None:
                if current_node.right is None:
                    tree1.append(None)
            current_node = current_node.right

        current_node = q
        while current_node or len(stack) > 0:
            while current_node:
                tree2_pre.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            if current_node.left is not None or current_node.right is not None:
                if current_node.left is None:
                    tree2.append(None)
            tree2.append(current_node.val)
            if current_node.left is not None or current_node.right is not None:
                if current_node.right is None:
                    tree2.append(None)
            current_node = current_node.right

        return tree1 == tree2 and tree1_pre == tree2_pre


# @lc code=end
        # pre
        tree1_pre, tree2_pre = list(), list()
        current_node = p
        while current_node or len(stack) > 0:
            while current_node:
                tree1_pre.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            current_node = current_node.right

        current_node = q
        while current_node or len(stack) > 0:
            while current_node:
                tree2_pre.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            current_node = current_node.right
