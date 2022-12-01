from queue import SimpleQueue as Queue, LifoQueue as Stack


INT_MAX = 2147483647


class Graph:
    adj_list: list[list[tuple]]
    vertices: list
    vnum: int

    def __init__(self, vnum, vertices=None) -> None:
        self.vnum = vnum
        if not vertices:
            self.vertices = range(vnum)
        else:
            self.vertices = vertices
        self.adj_list = [[] for i in range(vnum)]

    def print_adj(self):
        for i in range(self.vnum):
            print(self.vertices[i], end="")
            for v_i, w in self.adj_list[i]:
                print(f' -> ({self.vertices[v_i]}, {w})', end="")
            print('\n')

    def print_graph(self):
        print(f"Vertices list {self.vertices}")
        print(f"adjacent list: ")
        for i in self.adj_list:
            print(f"{i}")

    def add_edge(self, src, dest, weight, both_ways: bool = True):
        src_i = self.vertices.index(src)
        dest_i = self.vertices.index(dest)
        self.adj_list[src_i].append((dest_i, weight))
        if both_ways:
            self.adj_list[dest_i].append((src_i, weight))

    def bfs(self, start_v=None):
        visited = [False for i in range(self.vnum)]
        if start_v is not None:
            # case when user provided a starting point
            bfs_travel = []
            q = Queue()
            start_index = self.vertices.index(start_v)
            q.put(start_index)
            visited[start_index] = True

            while not q.empty():
                index = q.get()
                bfs_travel.append(index)

                for v_index, v_weight in self.adj_list[index]:
                    if not visited[v_index]:
                        q.put(v_index)
                        visited[v_index] = True
            return bfs_travel
        else:
            # case where user did not provide a starting point
            bfs_travel = []
            for v_index in range(self.vnum):
                if not visited[v_index]:
                    q = Queue()
                    q.put(v_index)
                    visited[v_index] = True
                    while not q.empty():
                        cur_vindex = q.get()
                        bfs_travel.append(self.vertices[cur_vindex])
                        for ev_index, ev_weight in self.adj_list[v_index]:
                            if not visited[ev_index]:
                                visited[ev_index] = True
                                q.put(ev_index)

            return bfs_travel

    def __dfs_util(self, v_indx, visited, dfs_travel):
        visited[v_indx] = True
        dfs_travel.append(self.vertices[v_indx])
        for neighbor, _ in self.adj_list[v_indx]:
            if not visited[neighbor]:
                self.__dfs_util(neighbor, visited, dfs_travel)

    def dfs(self, starting_v=None):
        visited = [False for i in range(self.vnum)]
        if starting_v is not None:
            dfs_travel = []
            starting_index = self.vertices.index(starting_v)
            self.__dfs_util(starting_index, visited, dfs_travel)
            return dfs_travel
        else:
            dfs_travel = []
            for v_index in range(self.vnum):
                if not visited[v_index]:
                    self.__dfs_util(v_index, visited, dfs_travel)
            return dfs_travel

# TODO: finish this late :(
    def dijsktra(self, starting_v, goal):
        starting_index = self.vertices.index(starting_v)
        goal_index = self.vertices.index(goal)
        dis = [INT_MAX for i in self.vertices]
        dis[starting_index] = 0
        pass


g = Graph(vnum=10)
g.add_edge(1, 3, 10)
g.add_edge(2, 3, 20)
g.add_edge(3, 5, 10)
g.add_edge(5, 6, 10)
g.add_edge(6, 9, 10)
g.add_edge(1, 2, 5)
g.add_edge(0, 4, 12)
g.add_edge(0, 1, 9)
g.print_graph()
bfs_travel = g.bfs()
dfs_travel = g.dfs()
print(bfs_travel)
print(dfs_travel)
