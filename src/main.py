from GraphInterface import GraphInteface


class NodeData:

    def __init__(self, tag=-1, info=""):
        self.id = id
        self.pos = {}
        self.tag = tag
        self.info = info
        self.in_edges = []  # not a None because then we won't be able to add edges- like null
        self.out_edges = []

    def __cmp__(self, other):
        return self.id == other.id

    def __str__(self):
        s = "id: " + self.id
        return s


    def getID(self)->int:
        return self.id


    def getPos(self):
        return self.pos


    def setPos(self, newPos):
        self.pos = newPos


    def getTag(self):
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info


    def getInEdges(self):
        return self.in_edges

    def getOutEdges(self):
        return self.out_edges





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


class DiGraph(GraphInteface): # None wont let us add things, tuple is const so i used dict
    def __init__(self, vertices_of_graph: dict = [], edges_of_graph: [] = None, v_size=0, edge_size=0,
                 mode_count=0):
        self.v_size = v_size
        self.edge_size = edge_size
        self.mode_count = mode_count
        self.vertices_of_graph = vertices_of_graph
        self.edges_of_graph = edges_of_graph

    # if we need banai maatik elizabeth

    def add_node(self, node_id: int, pos: tuple = {}) -> bool:
        if node_id in self.vertices_of_graph:
            node = id=node_id, pos=pos
            self.vertices_of_graph[node_id] = node
            self.v_size += 1
            self.mode_count += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.vertices_of_graph and id2 in self.vertices_of_graph:
            if not id2 in self.vertices_of_graph.get[id1].out_edges:
                edge = src=id1, dest=id2, weight=weight
                self.vertices_of_graph[id1].out_edges[id2] = edge
                self.vertices_of_graph[id2].in_edges[id1] = edge
                self.edge_size += 1
                self.mode_count += 1
                return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.vertices_of_graph:
            self.vertices_of_graph.pop(node_id)
            for e in self.all_out_edges_of_node(node_id):
                self.vertices_of_graph[EdgeData(e).dest].in_edges.pop(node_id)
                self.edge_size -= 1
            for e in self.all_in_edges_of_node(node_id):
                self.vertices_of_graph[EdgeData(e).src].out_edges.pop(node_id)
                self.edge_size -= 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.vertices_of_graph and node_id2 in self.vertices_of_graph:
            if node_id2 in self.vertices_of_graph[node_id1].out_edge:
                self.vertices_of_graph[node_id1].out_edges.pop(node_id2)
                return True
        return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph[id1].in_edges.values
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.vertices_of_graph:
            return self.vertices_of_graph[id1].out_edges.values
        return None

    def v_size(self) -> int:
        return self.v_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.mode_count
