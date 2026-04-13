# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root):
            if val < root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    dfs(root.left)
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    dfs(root.right)
        
        if root is None:
            return TreeNode(val)
        else:
            dfs(root)
            return root
            

    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root