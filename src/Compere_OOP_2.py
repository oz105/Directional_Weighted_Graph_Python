import time

import networkx as nx
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


if __name__ == '__main__':
    algo = GraphAlgo()
    file = '../data/compere/G_10_80_1.json'
    algo.load_from_json(file)
    start_time = time.time()
    # print(algo.shortest_path(1, 2000))
    algo.connected_components()
    print(time.time() - start_time, "seconds")

    # file_path = '../data/compere/G_10000_80000_1.json'
    algo.load_from_json(file)

    G = nx.DiGraph()
    for i in algo.get_graph().get_all_v().keys():
        G.add_node(i)
    for i in algo.get_graph().get_all_v().keys():
        for j, w in algo.get_graph().all_out_edges_of_node(i).items():
            G.add_edge(i, j, weight=w)

    start_time = time.time()
    # print(nx.dijkstra_path_length(G, 1, 54))
    # print(nx.dijkstra_path(G, 1, 2000))
    li = []
    for c in (nx.strongly_connected_components(G)):
        li.append(c)
    print(li)
    # print(nx.strongly_connected_components(G))
    print(time.time() - start_time, "seconds")


    # allg = GraphAlgo()
    # gg = DiGraph()
    #     # for i in range(12):
    #     #     gg.add_node(i)
    #     # gg.add_edge(0, 1, 3)
    #     # gg.add_edge(0, 3, 2)
    #     # gg.add_edge(1, 4, 1)
    #     # gg.add_edge(2, 6, 3)
    #     # gg.add_edge(3, 5, 1)
    #     # gg.add_edge(4, 1, 1)
    #     # gg.add_edge(4, 7, 2)
    #     # gg.add_edge(4, 11, 3)
    #     # gg.add_edge(5, 9, 2)
    #     # gg.add_edge(5, 11, 2)
    #     # gg.add_edge(5, 10, 3)
    #     # gg.add_edge(6, 0, 2)
    #     # gg.add_edge(6, 7, 2)
    #     # gg.add_edge(7, 9, 1)
    #     # gg.add_edge(8, 3, 4)
    #     # gg.add_edge(9, 4, 2)
    #     # gg.add_edge(9, 4, 2)
    #     # gg.add_edge(9, 11, 1)
    #     # gg.add_edge(10, 8, 1)
    #     # gg.add_edge(11, 6, 3)  # 19 edges
    # gg = DiGraph()
    # pos = [0, 0, 0]
    # for i in range(8):
    #     gg.add_node(i, pos)
    # gg.add_edge(0, 2, 2)
    # gg.add_edge(1, 0, 3)
    # gg.add_edge(1, 2, 1)
    # gg.add_edge(2, 3, 1)
    # gg.add_edge(3, 4, 2)
    # gg.add_edge(4, 6, 1)
    # gg.add_edge(6, 7, 2)
    # gg.add_edge(7, 1, 2)
    # gg.add_edge(5, 4, 1)
    # gg.add_edge(5, 6, 1)
    # allg.__init__(gg)
    #
    # G2 = nx.DiGraph()
    # for i in allg.get_graph().get_all_v().keys():
    #     G2.add_node(i)
    # for i in allg.get_graph().get_all_v().keys():
    #     for j, w in allg.get_graph().all_out_edges_of_node(i).items():
    #         G2.add_edge(i, j, weight=w)
    #
    # li = []
    # for c in (nx.strongly_connected_components(G2)):
    #     li.append(c)
    # print(li)

