#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result, stack = list(), list()
        if root:
            stack.append(root)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node:
                stack.append(current_node)
                stack.append(None)
                for each_node in current_node.children[::-1]:
                    if each_node:
                        stack.append(each_node)
            else:
                current_node = stack.pop()
                result.append(current_node.val)
        return result

# @lc code=end
