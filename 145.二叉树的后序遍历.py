#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result, slack = list(), list()
        if root:
            slack.append(root)
        while len(slack) > 0:
            current_node = slack.pop()
            if current_node:
                slack.append(current_node)
                slack.append(None)

                if current_node.right:
                    slack.append(current_node.right)
                if current_node.left:
                    slack.append(current_node.left)
            else:
                current_node = slack.pop()
                result.append(current_node.val)
        return result
# @lc code=end
