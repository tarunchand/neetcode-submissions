# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            top = stack.pop()
            if top is None:
                continue
            res.append(top.val)
            stack.append(top.right)
            stack.append(top.left)
        return res