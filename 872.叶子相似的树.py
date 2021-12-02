#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur_node: TreeNode, append_list: list):
        if cur_node:
            if cur_node.left or cur_node.right:
                self.dfs(cur_node.left, append_list)
                self.dfs(cur_node.right, append_list)
            else:
                append_list.append(cur_node.val)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        tree1_list, tree2_list = list(), list()
        self.dfs(root1, tree1_list)
        self.dfs(root2, tree2_list)
        return tree1_list == tree2_list
# @lc code=end
