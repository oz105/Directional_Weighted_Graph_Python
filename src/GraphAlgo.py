import math
import queue
from typing import List
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.main import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g :DiGraph = DiGraph):
        self.graph_algo = g

    def get_graph(self) -> GraphInterface:
        return self.graph_algo

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph_algo.vertices_of_graph.get(id1) is None or self.graph_algo.vertices_of_graph.get(id2) is None:
            return None
        path = []
        if id1 == id2:
            path.append(self.graph_algo.vertices_of_graph.get(id1)[1])
            return path
        src = self.graph_algo.vertices_of_graph.get(id1)[1]
        self.dijkstra(src)
        if self.graph_algo.vertices_of_graph.get(id2)[1].weight == math.inf:
            return None
        flag = True
        temp_key = self.graph_algo.vertices_of_graph.get(id2)[1]
        weight = temp_key.weight
        path.append(self.graph_algo.vertices_of_graph.get(id2)[1])
        while flag:
            temp_key = self.graph_algo.vertices_of_graph.get(temp_key.gets_from)[1]
            path.append(temp_key)
            if temp_key.id == id1:
                flag = False
        path.reverse()
        ans = (weight, path)
        return ans

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src):
        count_visit = 0
        q = queue.PriorityQueue()
        for n in self.graph_algo.get_all_v().values():
            n[1].tag = -1
            n[1].get_from = -1
            n[1].weight = math.inf

        if self.graph_algo.vertices_of_graph.get(src.id) is not None:
            src.tag = 1
            src.weight = 0
            src.get_from = src.id
            q.put(src)
            count_visit += 1

        while q.not_empty:
            temp_node = q.get()
            for d in self.graph_algo.all_out_edges_of_node(temp_node.id).keys():
                n = self.graph_algo.vertices_of_graph.get(d)[1]
                weight = temp_node.weight + self.graph_algo.vertices_of_graph.get(temp_node.id)[1].out_edges.get(d)
                if n.tag < 0 or n.weight > weight:
                    n.weight = weight
                    n.tag = 1
                    n.get_from = temp_node.id
                    q.put(n)
                    count_visit += 1

        return count_visit










