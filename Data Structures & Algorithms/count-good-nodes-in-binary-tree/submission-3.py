# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,highVal):
            if not node:
                return 0
            res= 1 if node.val >= highVal else 0
            highVal=max(node.val,highVal)
            res += dfs(node.left,highVal)
            res += dfs(node.right,highVal)
            return res
        return dfs(root, root.val)
        