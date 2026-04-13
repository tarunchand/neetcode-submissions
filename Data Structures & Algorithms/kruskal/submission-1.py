class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.num_components = n


    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        parent = self.find(self.parent[x])
        self.parent[x] = parent
        return parent
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return False
        rank_x = self.rank[parent_x]
        rank_y = self.rank[parent_y]
        if rank_x == rank_y:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1
        elif rank_x < rank_y:
            self.parent[parent_x] = parent_y
        elif rank_x > rank_y:
            self.parent[parent_y] = parent_x
        self.num_components -= 1
        return True
        

    def getNumComponents(self) -> int:
        return self.num_components


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Use min heap to sort the edges because we will not be using all the edges to form MST:- 
        # -> Heapify - O(E) (but the edges are not sorted yet)
        # -> Heap Pop (To sort) - O(klogk) where K = n - 1 since MST will have n - 1 edges. 
        # If we use any other sorting algorithm it will be O(ElogE) - Where E is total number of edges  
        edges.sort(key = lambda x : x[2])
        union_find = UnionFind(n)
        total_weight = 0
        for src, dst, weight in edges:
            if not union_find.isSameComponent(src, dst):
                union_find.union(src, dst)
                total_weight += weight
                if union_find.getNumComponents() == 1:
                    return total_weight
        return -1
