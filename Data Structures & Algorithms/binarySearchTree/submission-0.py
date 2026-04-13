class TreeNode:

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        
        def dfs_insert(root, key, val):
            if root is None:
                return TreeNode(key, val)
            if key < root.key:
                root.left = dfs_insert(root.left, key, val)
            elif key > root.key:
                root.right = dfs_insert(root.right, key, val)
            else:
                root.val = val
            return root

        self.root = dfs_insert(self.root, key, val)


    def get(self, key: int) -> int:
        
        def dfs_get(root, key):
            if root is None:
                return -1
            if key < root.key:
                return dfs_get(root.left, key)
            elif key > root.key:
                return dfs_get(root.right, key)
            else:
                return root.val

        return dfs_get(self.root, key)


    def dfs_get_min(self, root):
        if root is None:
            return -1, -1
        if root.left is None:
            return root.key, root.val
        return self.dfs_get_min(root.left)


    def getMin(self) -> int:
        return self.dfs_get_min(self.root)[1]


    def getMax(self) -> int:

        def dfs_get_max(root):
            if root is None:
                return -1
            if root.right is None:
                return root.val
            return dfs_get_max(root.right)

        return dfs_get_max(self.root)


    def remove(self, key: int) -> None:

        def dfs_remove(root, key):
            if root is None:
                return root
            if key < root.key:
                root.left = dfs_remove(root.left, key)
            elif key > root.key:
                root.right = dfs_remove(root.right, key)
            else:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    min_key, min_val = self.dfs_get_min(root.right)
                    root.key = min_key
                    root.val = min_val
                    root.right = dfs_remove(root.right, min_key)
            return root
        
        self.root = dfs_remove(self.root, key)


    def getInorderKeys(self) -> List[int]:
        inorder_keys = []

        def do_inorder_traversal(root):
            if root is None:
                return
            do_inorder_traversal(root.left)
            inorder_keys.append(root.key)
            do_inorder_traversal(root.right)

        do_inorder_traversal(self.root)
        return inorder_keys
            