import math
import unittest
from random import random

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    algo = GraphAlgo()



    def empty_graph_builder(self) -> DiGraph:
        gg = DiGraph()
        return gg

    def no_edges_graph_builder(self, size: int = 5):
        gg = DiGraph()
        for i in range(size):
            gg.add_node(i)
        return gg

    @staticmethod
    def whole_graph_builder(size: int = 5):
        gg = DiGraph()
        for i in range(size):
            gg.add_node(i)
        for i in range(size):
            for j in range(size):
                gg.add_edge(i, j, 1)

        return gg


    def specific_graph_builder(self):
        gg = DiGraph()
        pos = [0, 0, 0]
        for i in range(8):
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
        return gg

    def specific_big_graph_builder(self, size: int = 8):
        gg = DiGraph()
        for i in range(12):
            gg.add_node(i)
        gg.add_edge(0, 1, 3)
        gg.add_edge(0, 3, 2)
        gg.add_edge(1, 4, 1)
        gg.add_edge(2, 6, 3)
        gg.add_edge(3, 5, 1)
        gg.add_edge(4, 1, 1)
        gg.add_edge(4, 7, 2)
        gg.add_edge(4, 11, 3)
        gg.add_edge(5, 9, 2)
        gg.add_edge(5, 11, 2)
        gg.add_edge(5, 10, 3)
        gg.add_edge(6, 0, 2)
        gg.add_edge(6, 7, 2)
        gg.add_edge(7, 9, 1)
        gg.add_edge(8, 3, 4)
        gg.add_edge(9, 4, 2)
        gg.add_edge(9, 4, 2)
        gg.add_edge(9, 11, 1)
        gg.add_edge(10, 8, 1)
        gg.add_edge(11, 6, 3) # 19 edges
        return gg


    def specific_graph_random_weights(self):
        gg = DiGraph()
        pos = [0, 0, 0]
        for i in range(8):
            gg.add_node(node_id=i, pos=pos)
        gg.add_edge(0, 2, self.vSize * 2 + random())
        gg.add_edge(1, 0, self.vSize * 2 + random())
        gg.add_edge(1, 2, self.vSize * 2 + random())
        gg.add_edge(2, 3, self.vSize * 2 + random())
        gg.add_edge(3, 4, self.vSize * 2 + random())
        gg.add_edge(4, 6, self.vSize * 2 + random())
        gg.add_edge(6, 7, self.vSize * 2 + random())
        gg.add_edge(7, 1, self.vSize * 2 + random())
        gg.add_edge(5, 4, self.vSize * 2 + random())
        gg.add_edge(5, 6, self.vSize * 2 + random())
        return gg

    def test_init(self):
        self.algo.__init__(self.empty_graph_builder())
        self.assertEqual(0, self.algo.get_graph().e_size())
        self.assertEqual(0, self.algo.get_graph().v_size())
        self.algo.__init__(self.whole_graph_builder())
        self.assertEqual(25, self.algo.get_graph().e_size())
        self.assertEqual(5, self.algo.get_graph().v_size())
        self.algo.__init__(self.specific_big_graph_builder())
        self.assertEqual(19, self.algo.get_graph().e_size())
        self.assertEqual(12, self.algo.get_graph().v_size())

    def test_get_graph(self):
        self.algo.__init__(self.empty_graph_builder())
        gg = self.empty_graph_builder()
        self.assertEqual(gg, self.algo.get_graph())
        self.algo.__init__(self.specific_big_graph_builder())
        gg = self.specific_big_graph_builder()
        self.assertEqual(gg, self.algo.get_graph())
        self.algo.__init__(self.whole_graph_builder())
        gg = self.whole_graph_builder()
        self.assertEqual(gg, self.algo.get_graph())
        gg = self.specific_big_graph_builder()
        self.assertNotEqual(gg, self.algo.get_graph())

    def test_load_from_json_and_save_to_json(self):
        self.algo.__init__(self.empty_graph_builder())
        algo_load = GraphAlgo()
        self.algo.save_to_json("empty.json")
        algo_load.load_from_json("empty.json")
        self.assertEqual(algo_load.get_graph(), self.algo.get_graph())
        algo_load.get_graph().remove_node(0)
        self.assertEqual(algo_load.get_graph(), self.algo.get_graph())
        self.algo.__init__(self.whole_graph_builder())
        self.algo.save_to_json("whole.json")
        algo_load.load_from_json("whole.json")
        self.assertEqual(algo_load.get_graph(), self.algo.get_graph())
        algo_load.get_graph().remove_node(0)
        self.assertNotEqual(algo_load.get_graph(), self.algo.get_graph())
        self.algo.__init__(self.specific_big_graph_builder())
        self.algo.save_to_json("big specific graph.json")
        algo_load.load_from_json("big specific graph.json")
        self.assertEqual(algo_load.get_graph(), self.algo.get_graph())
        algo_load.get_graph().remove_node(1)
        self.assertNotEqual(algo_load.get_graph(), self.algo.get_graph())

    def test_shortest_path(self):
        self.algo.__init__(self.empty_graph_builder())
        self.assertEqual(math.inf, self.algo.shortest_path(0, 1)[0])
        self.assertEqual(math.inf, self.algo.shortest_path(1, 10)[0])
        self.assertEqual(math.inf, self.algo.shortest_path(5, 7)[0])
        self.algo.__init__(self.whole_graph_builder())
        self.assertEqual(1, self.algo.shortest_path(0, 3)[0])
        self.assertEqual(1, self.algo.shortest_path(1, 3)[0])
        self.assertEqual(1, self.algo.shortest_path(2, 4)[0])
        self.assertEqual(0, self.algo.shortest_path(2, 2)[0])
        self.assertEqual([2], self.algo.shortest_path(2, 2)[1])
        self.assertEqual(0, self.algo.shortest_path(1, 1)[0])
        self.assertEqual([1], self.algo.shortest_path(1, 1)[1])
        self.algo.__init__(self.specific_big_graph_builder())
        self.assertEqual(5, self.algo.shortest_path(0, 11)[0])
        self.assertEqual([0, 3, 5, 11], self.algo.shortest_path(0, 11)[1])
        self.assertEqual(2, self.algo.shortest_path(5, 9)[0])
        self.assertEqual([5, 9], self.algo.shortest_path(5, 9)[1])
        self.assertEqual(5, self.algo.shortest_path(2, 7)[0])
        self.assertEqual([2, 6, 7], self.algo.shortest_path(2, 7)[1])
        self.assertEqual(10, self.algo.shortest_path(10, 4)[0])
        self.assertEqual([10, 8, 3, 5, 9, 4], self.algo.shortest_path(10, 4)[1])
        self.algo.get_graph().add_edge(3, 4, 2)
        self.assertEqual(7, self.algo.shortest_path(10, 4)[0])
        self.assertEqual([10, 8, 3, 4], self.algo.shortest_path(10, 4)[1])
        self.algo.get_graph().add_edge(4, 5, 1)
        self.algo.get_graph().add_edge(11, 10, 2)
        self.assertEqual(6, self.algo.shortest_path(1, 8)[0])
        self.assertEqual([1, 4, 5, 10, 8], self.algo.shortest_path(1, 8)[1])
        self.algo.get_graph().remove_edge(4, 5)
        self.algo.get_graph().add_edge(4, 5, 3)
        self.assertEqual(7, self.algo.shortest_path(1, 8)[0])
        self.assertEqual([1, 4, 11, 10, 8], self.algo.shortest_path(1, 8)[1])
        self.algo.get_graph().remove_node(11)
        self.assertEqual(8, self.algo.shortest_path(1, 8)[0])
        self.assertEqual([1, 4, 5, 10, 8], self.algo.shortest_path(1, 8)[1])


if __name__ == '__main__':
    unittest.main()
