# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __go_left__(self):
        top = self.stack[-1]
        while top.left is not None:
            self.stack.append(top.left)
            top = top.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        if root is not None:
            self.stack.append(root)
            self.__go_left__()

    def next(self) -> int:
        top = self.stack.pop()
        if top.right is not None:
            self.stack.append(top.right)
            self.__go_left__()
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()