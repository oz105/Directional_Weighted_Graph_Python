import json
import math
import queue
from random import randrange
from matplotlib.patches import PathPatch, Path, Arrow
import numpy as np
import matplotlib.pyplot as plt
from typing import List
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph, NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph()):
        self.graph_algo = g

    def get_graph(self) -> GraphInterface:
        return self.graph_algo

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                temp_graph = DiGraph()
                json_dict = json.load(file)
                for n in json_dict["Nodes"]:
                    if len(n) == 1:
                        node = NodeData(n['id'])
                    else:
                        split = (n['pos'].split(","))
                        node = NodeData(n['id'], (float(split[0]), float(split[1])),float(split[2]))
                    temp_graph.add_node(node_id=node.id, pos=node.pos)
                for edge in json_dict['Edges']:
                    id1 = edge['src']
                    id2 = edge['dest']
                    w = edge['w']
                    temp_graph.add_edge(id1=id1, id2=id2, weight=w)
                self.graph_algo = temp_graph
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump((self.graph_algo.as_dict()), default=lambda m: m.as_dict(), indent=4, fp=file)
        except IOError as e:
            print(e)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph_algo.vertices_of_graph.get(id1) is None or self.graph_algo.vertices_of_graph.get(id2) is None:
            tup = (math.inf, [])
            return tup
        path = []
        if id1 == id2:
            path.append(self.graph_algo.vertices_of_graph.get(id1).id)
            tup = (0, path)
            return tup
        src = self.graph_algo.vertices_of_graph.get(id1)
        self.dijkstra(src)
        if self.graph_algo.vertices_of_graph.get(id2).weight == math.inf:
            tup = (math.inf, [])
            return tup
        flag = True
        temp_key = self.graph_algo.vertices_of_graph.get(id2)
        weight = temp_key.weight
        path.append(temp_key.id)
        while flag:
            temp_key = self.graph_algo.vertices_of_graph.get(temp_key.get_from)
            path.append(temp_key.id)
            if temp_key.id == id1:
                flag = False
        path.reverse()
        ans = (weight, path)
        return ans

    def connected_component(self, id1: int) -> list:
        final_list = []
        if self.graph_algo is None or id1 not in self.graph_algo.vertices_of_graph:
            return final_list
        return self.kosarajus(id1)

    def connected_components(self) -> List[list]:
        final_list = []
        if self.graph_algo is None or self.graph_algo.vertices_size == 0:
            return final_list
        if self.graph_algo.edge_size == 0:
            for node in self.graph_algo.vertices_of_graph.keys():
                solo_list = [node]
                final_list.append(solo_list)
            return final_list
        keys = {}
        for k in self.graph_algo.get_all_v().keys():
            keys[k] = 0
        for k in self.graph_algo.get_all_v().keys():
            if keys[k] == 0:
                keys[k] = 1
                scc = self.connected_component(k)
                final_list.append(scc)
                for key_node in scc:
                    keys[key_node] = 1
        return final_list

    def plot_graph(self) -> None:
        x_vals = []
        y_vals = []
        id_vals = []
        for n in self.graph_algo.get_all_v().values():
            if len(n.pos) == 0:
                tup = (randrange(25), randrange(25), randrange(25))
                n.pos = tup
            id_vals.append(n.id)
            x_vals.append(n.pos[0])
            y_vals.append(n.pos[1])
        fig, ax = plt.subplots()
        ax.scatter(x_vals, y_vals)
        if self.get_graph().v_size() < 20:
            for i, txt in enumerate(id_vals):
                ax.annotate(id_vals[i], (x_vals[i], y_vals[i]+0.05))
        if self.get_graph().v_size() > 20:
            for i, txt in enumerate(id_vals):
                ax.annotate(id_vals[i], (x_vals[i], y_vals[i]))
        plt.title("OOP 3")
        plt.plot(x_vals, y_vals, ".", color='black')
        for n in self.graph_algo.get_all_v().values():
            node = n
            src_x = (n.pos[0])
            src_y = (n.pos[1])
            for e in self.graph_algo.all_out_edges_of_node(node.id).keys():
                dest_node = self.graph_algo.vertices_of_graph.get(e)
                dest_x = (dest_node.pos[0])
                dest_y = (dest_node.pos[1])
                if self.get_graph().v_size() < 20:
                    plt.arrow(src_x, src_y, (dest_x - src_x), (dest_y - src_y), length_includes_head=True,
                              width=0.0003, head_width=0.3, color='red')
                if self.get_graph().v_size() > 20:
                    plt.arrow(src_x, src_y , (dest_x-src_x), (dest_y-src_y), length_includes_head=True,
                              width=0.00003, head_width=0.0003, color ='red')
        plt.show()

    def kosarajus(self, start: int):
        stack = [start]
        visited = {}
        opposite_visited = {}
        count_visited = 0
        for n in self.get_graph().get_all_v().keys():
            visited[n] = 0
            opposite_visited[n] = 0
        while len(stack) > 0:
            pop = stack.pop()
            if visited[pop] == 0:
                visited[pop] = 1
                count_visited += 1
                for neighbor in self.graph_algo.all_out_edges_of_node(pop).keys():
                    stack.append(neighbor)

        opposite_stuck = [start]
        count_opposite_visited = 0
        while len(opposite_stuck) > 0:
            pop = opposite_stuck.pop()
            if opposite_visited[pop] == 0:
                opposite_visited[pop] = 1
                count_opposite_visited += 1
                for neighbor in self.graph_algo.all_in_edges_of_node(pop).keys():
                    opposite_stuck.append(neighbor)
        final_list = []
        if count_visited > count_opposite_visited:
            for k in visited.keys():
                if opposite_visited[k] == 1:
                    final_list.append(k)
        else:
            for k in opposite_visited.keys():
                if visited[k] == 1:
                    final_list.append(k)
        return final_list

    def dijkstra(self, src):
        count_visit = 0
        q = queue.PriorityQueue()
        for n in self.graph_algo.get_all_v().values():
            n.tag = -1
            n.get_from = -1
            n.weight = math.inf

        if self.graph_algo.vertices_of_graph.get(src.id) is not None:
            src.tag = 1
            src.weight = 0
            src.get_from = src.id
            q.put(src)
            count_visit += 1

        while not q.empty():
            temp_node = q.get()
            for d in self.graph_algo.all_out_edges_of_node(temp_node.id).keys():
                n = self.graph_algo.vertices_of_graph.get(d)
                weight = temp_node.weight + self.graph_algo.vertices_of_graph.get(temp_node.id).out_edges.get(d)
                if n.tag < 0 or n.weight > weight:
                    n.weight = weight
                    n.tag = 1
                    n.get_from = temp_node.id
                    q.put(n)
                    if n.tag < 0:
                        count_visit += 1
        return count_visit

