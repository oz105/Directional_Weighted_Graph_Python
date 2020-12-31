import unittest
from random import random

from src.main import NodeData, EdgeData, DiGraph

class GraphTests:
    vSize = 10



    def nextRnd(self, min = 0, max = 100):
        seed = 30
        d = random(seed).nextDouble();
        dx = max - min;
        ans = d * dx + min;
        return ans;

    def empty_graph_builder(self)->DiGraph:
        gg = DiGraph()
        pos = [0, 0, 0]
        for i in range (GraphTests.vSize):
            gg.add_node(i,pos)

    def whole_graph_builder(self):
        gg = DiGraph()
        pos = [0, 0, 0]
        for i in range (GraphTests.vSize):
            gg.add_node(i,pos)
        for i in range (GraphTests.vSize):
            for j in range (GraphTests.vSize):
                gg.add_edge(i, j, GraphTests.vSize*2 + random())

    def specific_graph_builder(self):
        gg = DiGraph()
        pos = [0, 0, 0]
        for i in range(8):
            gg.add_node(i, pos)
        gg.add_edge(0, 2, GraphTests.vSize * 2 + random())
        gg.add_edge(1, 0, GraphTests.vSize * 2 + random())
        gg.add_edge(1, 2, GraphTests.vSize * 2 + random())
        gg.add_edge(2, 3, GraphTests.vSize * 2 + random())
        gg.add_edge(3, 4, GraphTests.vSize * 2 + random())
        gg.add_edge(4, 6, GraphTests.vSize * 2 + random())
        gg.add_edge(6, 7, GraphTests.vSize * 2 + random())
        gg.add_edge(7, 1, GraphTests.vSize * 2 + random())
        gg.add_edge(5, 4, GraphTests.vSize * 2 + random())
        gg.add_edge(5, 6, GraphTests.vSize * 2 + random())
        return gg







    def test_v_size(self):
        g = GraphTests.empty_graph_builder()
        self.assertTrue(g.v_size==GraphTests.vSize)
        g.add_node(GraphTests.vSize+1)
        self.assertTrue(g.v_size == GraphTests.vSize+1)
        g.remove_node(GraphTests.vSize + 1)
        g.remove_node(0)
        self.assertTrue(g.v_size == GraphTests.vSize-1)

    def test_e_size(self):
        g = GraphTests.specific_graph_builder()
        self.assertTrue(g.e_size==10)
        g.remove_edge(1, 0)
        self.assertTrue(g.v_size == 9)
        g.add_edge(1, 7, 0)
        g.add_edge(0, 7, 0)
        self.assertTrue(g.v_size == 11)


    def test_get_all_v(self):
        g = GraphTests.empty_graph_builder()
        # arr = [i in range (DiGraph.v_size)]
        # מערך בגודל מספר הקודקודים שמאותחל להיות כולו 0
        # אבל צריך לעשותאת זה iterable ולא הצלחתי









