from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.rightSideViewDFS(root)

    def rightSideViewDFS(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, depth):
            if root is None:
                return
            if depth == len(res):
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return res


    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            res.append(q[-1].val)
            for _ in range(q_len):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        
        return res