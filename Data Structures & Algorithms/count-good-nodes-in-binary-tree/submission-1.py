# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0

        def check(node, highest):
            if node.val >= highest:
                self.count += 1

        def dfs(node, highest):
            if not node:
                return

            check(node, highest)
            highest = max(highest, node.val)
            dfs(node.left, highest)
            dfs(node.right, highest)

        dfs(root, root.val)
        return self.count