"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:

        old_to_new_map = dict()

        def dfs(root):
            if root in old_to_new_map:
                return old_to_new_map[root]
            cloned_node = Node(root.val)
            old_to_new_map[root] = cloned_node
            for neighbor in root.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            return clone_node

        return dfs(node) if root is not None else None

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        visit_mapping = dict()
        visit = set()
        
        def dfs(root, cloned_node):
            if root in visit:
                return None
            visit_mapping[root] = cloned_node
            visit.add(root)
            for neighbor in root.neighbors:
                clone_neighbor_node = visit_mapping.get(neighbor, Node(neighbor.val))
                visit_mapping[neighbor] = clone_neighbor_node
                cloned_node.neighbors.append(clone_neighbor_node)
            for i in range(len(root.neighbors)):
                dfs(root.neighbors[i], cloned_node.neighbors[i])
            return cloned_node

        return dfs(node, Node(node.val))

