# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr=[]
        final=0
        def dfs(node):
            if not node:
                return 0
            else:
                self.arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(f"arr before sorting:{self.arr}")
        self.arr=sorted(self.arr)
        print(f"arr after sorting:{self.arr}")
        return self.arr[k-1]