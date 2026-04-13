# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        # 0 - No sub-tree visited, 1 - Left sub-tree visited, 2 - Right sub-tree visited
        stack = [(root, 0)]
        res = []
        while stack:
            top_root, top_visit_flag = stack[-1]
            if top_root is None:
                stack.pop()
                continue
            if top_visit_flag == 2: # Right sub-tree is also visited
               res.append(top_root.val)
               stack.pop()
            elif top_visit_flag == 1: # Left sub-tree is visited. Visit Right sub-tree
                stack[-1] = (top_root, 2) # Mark top of stack as right sub tree visited and visit right
                stack.append((top_root.right, 0))
            else: # No sub-tree is visited. Visit Left sub-tree
                stack[-1] = (top_root, 1) # Mark top of stack as left sub tree visited and visit left
                stack.append((top_root.left, 0))
        return res