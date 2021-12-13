# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,treenode:TreeNode):
        if self.result:
            if treenode:
                if treenode.val != self.val:
                    self.result = False
                    return None
                self.dfs(treenode.left)
                self.dfs(treenode.right)

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.result = True
        self.val = root.val
        self.dfs(root)
        return self.result