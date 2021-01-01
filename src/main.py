from src.GraphInterface import GraphInteface


# need to check function remove_node

class NodeData:

    def __init__(self, id, pos: tuple = (), tag=-1, info=""):
        self.id = id
        self.pos = pos
        self.tag = tag
        self.info = info
        self.in_edges = {}
        self.out_edges = {}

    def __cmp__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"id: {self.id}"


class EdgeData:

    def __init__(self, src, dest, weight, tag=0):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = tag

    def __cmp__(self, other):
        return self.src == other.src and self.dest == other.dest

    def __str__(self):
        return self.src + "->" + self.dest + ",weight: " + self.weight


class DiGraph(GraphInteface):

    def __init__(self, v_size=0, edge_size=0, mode_count=0):
        self.vertices_size = v_size
        self.edge_size = edge_size
        self.mode_count = mode_count
        self.vertices_of_graph = {}
        self.edges_of_graph = {}

    def add_node(self, node_id: int, pos: tuple = ()) -> bool:
        if not node_id in self.vertices_of_graph:
            node = NodeData(id=node_id)
            self.vertices_of_graph[node_id] = node
            self.vertices_size += 1
            self.mode_count += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.vertices_of_graph and id2 in self.vertices_of_graph:
            if not id2 in self.vertices_of_graph[id1].out_edges:
                edge = EdgeData(src=id1, dest=id2,weight=weight)
                self.vertices_of_graph[id1].out_edges[id2] = edge
                self.vertices_of_graph[id2].in_edges[id1] = edge
                self.edge_size += 1
                self.mode_count += 1
                return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.vertices_of_graph:
            if self.all_out_edges_of_node(node_id) != None:
                for e in self.all_out_edges_of_node(node_id):
                    self.vertices_of_graph[e.dest].in_edges.pop(node_id)
                    self.edge_size -= 1
            if self.all_in_edges_of_node(node_id) != None:
                for e in self.all_in_edges_of_node(node_id):
                    self.vertices_of_graph[e.src].out_edges.pop(node_id)
                    self.edge_size -= 1
            self.vertices_of_graph.pop(node_id)
            self.vertices_size -= 1
            self.mode_count += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.vertices_of_graph and node_id2 in self.vertices_of_graph:
            if node_id2 in self.vertices_of_graph[node_id1].out_edges:
                self.vertices_of_graph[node_id1].out_edges.pop(node_id2)
                self.edge_size -= 1
                self.mode_count += 1
                return True
        return False

    def get_all_v(self) -> dict:
        return self.vertices_of_graph.values()

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph[id1].in_edges.values
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph[id1].out_edges.values
        return None

    def v_size(self) -> int:
        return self.vertices_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.mode_count

    def __str__(self):
        res = ""
        for i in self.get_all_v():
            print(i.out_edges.values)
            res = f"str :{i} -> "

        return res

