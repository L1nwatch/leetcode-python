#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, tree_node: TreeNode, sub_node: TreeNode) -> bool:
        if not tree_node and not sub_node:
            return True
        if not tree_node or not sub_node or tree_node.val != sub_node.val:
            return False
        return self.check(tree_node.left, sub_node.left) and self.check(tree_node.right, sub_node.right)

    def dfs(self, root_node: TreeNode, sub_node: TreeNode):
        if not root_node:
            return False
        return self.check(root_node, sub_node) or self.dfs(root_node.left, sub_node) or self.dfs(root_node.right, sub_node)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return self.dfs(root, subRoot)
# @lc code=end
