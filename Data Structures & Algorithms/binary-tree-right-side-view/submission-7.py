# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        q.append(root)
        if not root:
            return []

        while q:
            level=[]
            for i in range(0, len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        print(f"res:{res}")
        print(f"length of res:{len(res)}")
        final=[]
        for i in range(len(res)):
            final.append(res[i][-1])
        print(f"final:{final}")

        return final
