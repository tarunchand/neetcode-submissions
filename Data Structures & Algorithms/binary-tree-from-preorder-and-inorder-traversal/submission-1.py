# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # A clever way is to keep building the sub-tree from the pre-order list until you reach 
    # the parent of the subtree in the inorder map.  
    # Core idea :- 
    # Preorder tells you what node to create next
    # Inorder tells you when to stop building a subtree
    # You keep creating nodes until you hit the parent’s value in inorder
    # That parent value means: Stop. This subtree is finished.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_ord_idx = in_ord_idx = 0

        def dfs(parent):
            nonlocal pre_ord_idx, in_ord_idx
            if pre_ord_idx == len(preorder):
                return None
            if inorder[in_ord_idx] == parent:
                in_ord_idx += 1
                return None
            root = TreeNode(preorder[pre_ord_idx])
            pre_ord_idx += 1
            root.left = dfs(root.val)
            root.right = dfs(parent)
            return root

        return dfs(float('inf'))

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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