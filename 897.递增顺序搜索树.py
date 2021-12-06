#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, pre_node = None, None
        stack = list()
        if root:
            stack.append(root)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node:
                if current_node.right:
                    stack.append(current_node.right)

                stack.append(current_node)
                stack.append(None)

                if current_node.left:
                    stack.append(current_node.left)
            else:
                current_node = stack.pop()
                current_node.left = current_node.right = None

                if head:
                    pre_node.right = current_node
                    pre_node = current_node
                else:
                    head = pre_node = current_node
        return head
# @lc code=end

