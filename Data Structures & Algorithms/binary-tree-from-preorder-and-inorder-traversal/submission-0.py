# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = dict()
        for i, val in enumerate(inorder):
            inorder_index_map[val] = i

        pre_order_index = 0

        def buildTree(left, right):
            nonlocal pre_order_index
            if left > right:
                return None
            cur_val = preorder[pre_order_index]
            pre_order_index += 1
            root = TreeNode(cur_val)
            inorder_index = inorder_index_map[cur_val]
            root.left = buildTree(left, inorder_index - 1)
            root.right = buildTree(inorder_index + 1, right)
            return root

        return buildTree(0, len(preorder) - 1)