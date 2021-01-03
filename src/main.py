from src.GraphInterface import GraphInterface


# need to check function remove_node

class NodeData:

    def __init__(self, id, pos: tuple = (0, 0), tag=-1, info=""):
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


# class EdgeData:
#
#     def __init__(self, src, dest, weight, tag=0):
#         self.src = src
#         self.dest = dest
#         self.weight = weight
#         self.tag = tag
#
#     def __cmp__(self, other):
#         return self.src == other.src and self.dest == other.dest
#
#     def __str__(self):
#         return self.src + "->" + self.dest + ",weight: " + self.weight


class DiGraph(GraphInterface):

    def __init__(self, v_size=0, edge_size=0, mode_count=0):
        self.vertices_size = v_size
        self.edge_size = edge_size
        self.mode_count = mode_count
        self.vertices_of_graph = {}
        self.edges_of_graph = {}

    def add_node(self, node_id: int, pos: tuple = (0, 0)) -> bool:
        if node_id not in self.vertices_of_graph:
            node = NodeData(id=node_id, pos=pos)
            tup = (node_id, node)
            self.vertices_of_graph[node_id] = tup
            self.vertices_size += 1
            self.mode_count += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.vertices_of_graph and id2 in self.vertices_of_graph:
            if id2 not in self.vertices_of_graph.get(id1)[1].out_edges:
                # edge = EdgeData(src=id1, dest=id2,weight=weight)
                tup = (id2, weight)
                self.vertices_of_graph.get(id1)[1].out_edges[id2] = tup
                tup = (id1, weight)
                self.vertices_of_graph.get(id2)[1].in_edges[id1] = tup
                self.edge_size += 1
                self.mode_count += 1
                return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.vertices_of_graph:
            if self.all_out_edges_of_node(node_id).keys() is not None:
                for k in self.all_out_edges_of_node(node_id).keys():
                    self.vertices_of_graph.get(k)[1].in_edges.pop(node_id)
                    self.edge_size -= 1
            if self.all_in_edges_of_node(node_id).keys() is not None:
                for k in self.all_in_edges_of_node(node_id).keys():
                    self.vertices_of_graph.get(k)[1].out_edges.pop(node_id)
                    self.edge_size -= 1
            self.vertices_of_graph.pop(node_id)
            self.vertices_size -= 1
            self.mode_count += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.vertices_of_graph and node_id2 in self.vertices_of_graph:
            if node_id2 in self.vertices_of_graph.get(node_id1)[1].out_edges:
                self.vertices_of_graph.get(node_id1)[1].out_edges.pop(node_id2)
                self.vertices_of_graph.get(node_id2)[1].in_edges.pop(node_id1)
                self.edge_size -= 1
                self.mode_count += 1
                return True
        return False

    def get_all_v(self) -> dict:
        return self.vertices_of_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph.get(id1)[1].in_edges
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph.get(id1)[1].out_edges
        return None

    def v_size(self) -> int:
        return self.vertices_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.mode_count

    def __str__(self):

        res = ""
        for i in self.get_all_v().keys():
            res += f"{i} -> ["
            for j in self.vertices_of_graph.get(i)[1].out_edges.keys():
                res += f"{j},"
            res += "]\n"

        return res

