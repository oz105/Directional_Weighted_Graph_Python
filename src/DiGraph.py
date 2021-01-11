from filecmp import cmp

from src.GraphInterface import GraphInterface


class NodeData:

    def __init__(self, node_id, pos: tuple = (), tag=-1, weight: int = 0):
        self.id = node_id
        self.pos = pos
        self.tag = tag
        self.weight = weight
        self.get_from = -1
        self.in_edges = {}
        self.out_edges = {}

    def __eq__(self, other):
        if other is None:
            if self is not None:
                return False
            else:
                return True
        if self is None:
            return False
        return self.id == other.id and self.pos == other.pos

    def __repr__(self):
        return f"id: {self.id} , pos: {self.pos}"

    def __str__(self):
        return f"id: {self.id}"

    def __lt__(self, other):
        return self.weight < other.weight

    def __cmp__(self, other):
        return cmp(self.weight, other.weight)

    def as_dict(self):
        res_dict = self.__dict__.copy()
        try:
            del res_dict["tag"]
            del res_dict["in_edges"]
            del res_dict["out_edges"]
            del res_dict["get_from"]
            del res_dict["weight"]
        except IOError as e:
            print(e)

        return res_dict

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

    def __init__(self):
        self.vertices_size = 0
        self.edge_size = 0
        self.mode_count = 0
        self.vertices_of_graph = {}

    def add_node(self, node_id: int, pos: tuple = ()) -> bool:
        if node_id not in self.vertices_of_graph:
            node = NodeData(node_id=node_id, pos=pos)
            self.vertices_of_graph[node_id] = node
            self.vertices_size += 1
            self.mode_count += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.vertices_of_graph and id2 in self.vertices_of_graph:
            if id2 not in self.vertices_of_graph.get(id1).out_edges:
                self.vertices_of_graph.get(id1).out_edges[id2] = weight
                self.vertices_of_graph.get(id2).in_edges[id1] = weight
                self.edge_size += 1
                self.mode_count += 1
                return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.vertices_of_graph:
            if self.all_out_edges_of_node(node_id).keys() is not None:
                for k in self.all_out_edges_of_node(node_id).keys():
                    self.vertices_of_graph.get(k).in_edges.pop(node_id)
                    self.edge_size -= 1
            if self.all_in_edges_of_node(node_id).keys() is not None:
                for k in self.all_in_edges_of_node(node_id).keys():
                    self.vertices_of_graph.get(k).out_edges.pop(node_id)
                    self.edge_size -= 1
            self.vertices_of_graph.pop(node_id)
            self.vertices_size -= 1
            self.mode_count += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.vertices_of_graph and node_id2 in self.vertices_of_graph:
            if node_id2 in self.vertices_of_graph.get(node_id1).out_edges:
                self.vertices_of_graph.get(node_id1).out_edges.pop(node_id2)
                self.vertices_of_graph.get(node_id2).in_edges.pop(node_id1)
                self.edge_size -= 1
                self.mode_count += 1
                return True
        return False

    def get_all_v(self) -> dict:
        return self.vertices_of_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph.get(id1).in_edges
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph.get(id1).out_edges
        return None

    def v_size(self) -> int:
        return self.vertices_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.mode_count

    def as_dict(self):
        try:
            nodes = []
            new_dict = {}
            for n in self.get_all_v().values():
                if len(n.pos) == 0:
                    node = {'id': n.id}
                elif len(n.pos) == 2:
                    node = {'id': n.id, 'pos': f"{n.pos[0]},{n.pos[1]}"}
                else:
                    node = {'id': n.id, 'pos': f"{n.pos[0]},{n.pos[1]},{n.pos[2]}"}
                nodes.append(node)
            new_dict['Nodes'] = nodes
            edges = []
            for k in self.vertices_of_graph.keys():
                for dest, weight in self.all_in_edges_of_node(k).items():
                    edge = {'src': k, 'dest': dest, 'w': weight}
                    edges.append(edge)
            new_dict['Edges'] = edges
        except IOError as e:
            print(e)
        return new_dict

    def __eq__(self, other):
        if other is None or self.__class__ != other.__class__:
            return False
        if self.v_size() != other.v_size() or self.e_size() != other.e_size():
            return False
        return self.vertices_of_graph.__eq__(other.vertices_of_graph)

    def __str__(self):
        res = ""
        for i in self.get_all_v().keys():
            res += f"{i} -> ["
            for j in self.vertices_of_graph.get(i).out_edges.keys():
                res += f"{j},"
            res += "]\n"

        return res

