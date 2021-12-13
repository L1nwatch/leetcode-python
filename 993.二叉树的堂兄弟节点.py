#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur_treenode: TreeNode, depth: int, pre_node: TreeNode):
        if cur_treenode and not self.answer:
            if cur_treenode.val == self.x:
                self.x_pre = pre_node
                self.x_depth = depth
                if self.y_depth is not None:
                    self.answer = (self.y_pre != self.x_pre and self.x_depth == self.y_depth)
            elif cur_treenode.val == self.y:
                self.y_pre = pre_node
                self.y_depth = depth
                if self.x_depth is not None:
                    self.answer = (self.y_pre != self.x_pre and self.x_depth == self.y_depth)
            self.dfs(cur_treenode.left, depth+1, cur_treenode)
            self.dfs(cur_treenode.right, depth+1, cur_treenode)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x, self.y = x, y
        self.x_pre, self.y_pre = None, None
        self.x_depth, self.y_depth = None, None
        self.answer = None
        self.dfs(root, 0, None)
        return self.answer
# @lc code=end
