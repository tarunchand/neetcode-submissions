# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')

        def dfs(node):
            nonlocal maxi
            if node is None:
                return float('-inf')
            if node.left is None and node.right is None:
                maxi = max(maxi, node.val)
                return node.val
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            maxi = max(maxi, node.val, node.val + left_max, node.val + right_max, node.val + left_max + right_max)
            return max(node.val, node.val + left_max, node.val + right_max)

        dfs(root)
        return maxi
