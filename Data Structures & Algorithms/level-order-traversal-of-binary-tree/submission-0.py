from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            cur_level_len = len(q)
            cur_level = []
            while cur_level_len > 0:
                node = q.popleft()
                cur_level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                cur_level_len -= 1
            if cur_level:
                res.append(cur_level)

        return res