#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_val = 10 **5
        stack = list()
        if root:
            stack.append(root)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node:
                if current_node.left:
                    stack.append(current_node.left)

                    sub = abs(current_node.left.val-current_node.val)
                    if sub < min_val:
                        min_val = sub
                if current_node.right:
                    stack.append(current_node.right)

                    sub = abs(current_node.right.val-current_node.val)
                    if sub < min_val:
                        min_val = sub
                stack.append(current_node)
                stack.append(None)
            else:
                current_node = stack.pop()
        return min_val
# @lc code=end

