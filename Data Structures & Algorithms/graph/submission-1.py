class Graph:
    
    def __init__(self):
        self.adj_list = dict()

    def addEdge(self, src: int, dst: int) -> None:
        if src in self.adj_list:
            self.adj_list[src].add(dst)
        else:
            initial_set = set()
            initial_set.add(dst)
            self.adj_list[src] = initial_set

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adj_list:
            if dst in self.adj_list[src]:
                self.adj_list[src].remove(dst)
                return True
            else:
                return False
        else:
            return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = dict()

        def dfs(cur_src):
            if cur_src == dst:
                return True
            if cur_src not in self.adj_list:
                return False
            if cur_src in visited:
                return False

            visited[cur_src] = True            
            result = False
            for edge in self.adj_list[cur_src]:
                result = result or dfs(edge)

            return result

        return dfs(src)
