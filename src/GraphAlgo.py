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
                    node = NodeData(n['id'], n['pos'])
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
            path.append(self.graph_algo.vertices_of_graph.get(id1)[1].id)
            tup = (0, path)
            return tup
        src = self.graph_algo.vertices_of_graph.get(id1)[1]
        self.dijkstra(src)
        if self.graph_algo.vertices_of_graph.get(id2)[1].weight == math.inf:
            tup = (math.inf, [])
            return tup
        flag = True
        temp_key = self.graph_algo.vertices_of_graph.get(id2)[1]
        weight = temp_key.weight
        path.append(temp_key.id)
        while flag:
            temp_key = self.graph_algo.vertices_of_graph.get(temp_key.get_from)[1]
            path.append(temp_key.id)
            if temp_key.id == id1:
                flag = False
        path.reverse()
        ans = (weight, path)
        return ans

    def connected_component(self, id1: int) -> list:
        return_list = list.__init__()
        if self.graph_algo == None or (not self.graph_algo.vertices_of_graph.__contains__(id1)):
            return return_list
        node = self.graph_algo.vertices_of_graph.get(id1)
        for n in self.graph_algo.vertices_of_graph:
            n.tag = -1
        counter = 0
        temp = None
        q1 = queue.SimpleQueue
        q1.add(node)
        counter = 1
        q1f = queue.PriorityQueue
        while q1.qsize()>0:
            if q1.peek() != None:
                if temp != None:
                    q1f.put(temp)
                temp = q1.poll()
            for e in self.graph_algo.getE(temp.id):
                n2 = self.graph_algo.vertices_of_graph.get(e.getDest())
                if n2.getTag() == -1:
                    counter+=1
                    if self.graph_algo.getE(n2.id) != None:
                        q1.add(n2)
                        n2.setTag(1)
        temp = None
        q2 = queue.SimpleQueue
        q2f = queue.PriorityQueue
        q2.add(node)
        counter = 1
        while q2.qsize()>0:
            if q2.peek() != None:
                if temp != None:
                    q2f.add(temp)
                temp = q2.poll()
        for e in self.graph_algo.all_in_edges_of_node(temp.id):
            n2 = self.graph_algo.vertices_of_graph.get(e.getDest)
            if n2.tag == 1:
                counter+=1
                if self.graph_algo.all_in_edges_of_node(n2.id) != None:
                    q2.add(n2)
                    n2.setTag(2)

        b = q2f.qsize()>0 and q1f.qsize()>0
        l1 = q1f.qsize()
        l2 = q2f.qsize()
        n1 = q1f.get()
        n2 = q2f.get()
        while b:
            if n1 == n2:
                l1-=1
                l2-=1
                return_list.insert(n1)
            elif n2.id < n1.id:
                l1+=1
                if l1==0:
                    return return_list
                n1 = q1f.get()
            else:
                l2+=1
                if l2 == 0:
                    return return_list
                n2 = q2f.get()
        return return_list


    def connected_components(self) -> List[list]:
        return_list = list.__init__()
        if self.graph_algo == None:
            return return_list
        q_vertices = queue.SimpleQueue

        for node in self.graph_algo.vertices_of_graph:
            q_vertices.put(node)

        while q_vertices.qsize() > 0:
            temp_list = GraphAlgo.connected_component(q_vertices.get().id)
            return_list.put(temp_list)
            for node in temp_list:
                q_vertices.get(node)
        return return_list


    def plot_graph(self) -> None:
        x_vals = []
        y_vals = []
        z_vals = []
        for n in self.graph_algo.get_all_v().values():
            if len(n[1].pos) > 0:
                x_vals.append(n[1].pos[0])
                y_vals.append(n[1].pos[1])
        print(x_vals)
        print(y_vals)
        print(z_vals)
        plt.title("Ex3-OOP")
        plt.xlabel("x values")
        plt.ylabel("y values")
        plt.plot(x_vals,y_vals, "o")
        plt.show()











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

        while not q.empty():
            temp_node = q.get()
            for d in self.graph_algo.all_out_edges_of_node(temp_node.id).keys():
                n = self.graph_algo.vertices_of_graph.get(d)[1]
                weight = temp_node.weight + self.graph_algo.vertices_of_graph.get(temp_node.id)[1].out_edges.get(d)[1]
                if n.tag < 0 or n.weight > weight:
                    n.weight = weight
                    n.tag = 1
                    n.get_from = temp_node.id
                    q.put(n)
                    count_visit += 1
        return count_visit


if __name__ == '__main__':
        gg = DiGraph()
        for i in range(8):
            pos = (randrange(10), randrange(6))
            gg.add_node(i, pos)
        gg.add_edge(0, 2, 2)
        gg.add_edge(1, 0, 3)
        gg.add_edge(1, 2, 1)
        gg.add_edge(2, 3, 1)
        gg.add_edge(3, 4, 2)
        gg.add_edge(4, 6, 1)
        gg.add_edge(6, 7, 2)
        gg.add_edge(7, 1, 2)
        gg.add_edge(5, 4, 1)
        gg.add_edge(5, 6, 1)

        algo = GraphAlgo(gg)
        algo.save_to_json("first.json")
        algo.load_from_json("A0")
        print(algo.graph_algo)
        algo.plot_graph()


