import unittest
from random import random

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    vSize = 10

    def empty_graph_builder(self) -> DiGraph:
        gg = DiGraph()
        return gg

    def no_edges_graph_builder(self, size: int = 5):
        gg = DiGraph()
        for i in range(size):
            gg.add_node(i)
        return gg

    def whole_graph_builder(self, size: int = 5):
        gg = DiGraph()
        for i in range(size):
            gg.add_node(i)
        for i in range(size):
            for j in range(size):
                gg.add_edge(i, j, 1)

        return gg

    def specific_graph_builder(self, size: int = 8):
        gg = DiGraph()
        pos = [0, 0, 0]
        for i in range(size):
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

    def test_v_size(self):
        empty_graph = self.empty_graph_builder()
        self.assertEqual(empty_graph.v_size(), 0)
        empty_graph.add_node(1)
        self.assertEqual(empty_graph.v_size(), 1)
        empty_graph.add_node(2)
        self.assertNotEqual(empty_graph.v_size(), 1)
        self.assertEqual(empty_graph.v_size(), 2)
        empty_graph.remove_node(1)
        self.assertEqual(empty_graph.v_size(), 1)
        empty_graph.remove_node(2)
        self.assertEqual(empty_graph.v_size(), 0)
        g = self.no_edges_graph_builder()
        self.assertTrue(g.v_size() == 5)
        g.add_node(6)
        self.assertTrue(g.v_size() == 6)
        g.remove_node(6)
        g.remove_node(0)
        self.assertTrue(g.v_size() == 4)

    def test_e_size(self):
        g = self.specific_graph_random_weights()
        self.assertTrue(g.e_size() == 10)
        g.remove_edge(1, 0)
        self.assertTrue(g.e_size() == 9)
        g.add_edge(1, 7, 0)
        g.add_edge(0, 7, 0)
        self.assertTrue(g.e_size() == 11)
        empty_graph = self.empty_graph_builder()
        self.assertEqual(empty_graph.e_size(), 0)

    def test_MC(self):
        g = self.empty_graph_builder()
        self.assertEqual(g.get_mc(), 0)
        g.add_node(0)
        self.assertEqual(g.get_mc(), 1)
        g.add_node(1)
        self.assertEqual(g.get_mc(), 2)
        g.remove_node(0)
        self.assertEqual(g.get_mc(), 3)
        g.add_node(0)
        g.add_edge(1, 0, 1)
        g.add_edge(0, 1, 1)
        self.assertEqual(g.get_mc(), 6)
        g.remove_edge(0, 1)
        self.assertEqual(g.get_mc(), 7)

    def test_add_node(self):
        g = self.specific_graph_builder()
        self.assertFalse(g.add_node(0))
        self.assertFalse(g.add_node(1))
        self.assertFalse(g.add_node(2))
        self.assertTrue(g.add_node(9))
        self.assertTrue(g.add_node(10))
        g = self.empty_graph_builder()
        self.assertTrue(g.add_node(0))

    def test_add_edge(self):
        g = self.specific_graph_builder()
        self.assertFalse(g.add_edge(0, 2, 2))
        self.assertFalse(g.add_edge(0, 2, 3))
        self.assertFalse(g.add_edge(8, 7, 2))
        self.assertFalse(g.add_edge(6, 7, 2))
        self.assertTrue(g.add_edge(3, 7, 1))
        self.assertTrue(g.add_edge(1, 4, 1))

    def test_remove_edge(self):
        g = self.specific_graph_builder()
        self.assertFalse(g.remove_edge(0, 1))
        self.assertFalse(g.remove_edge(2, 1))
        g = self.specific_graph_builder()
        self.assertTrue(g.remove_edge(1, 2))
        self.assertTrue(g.remove_edge(0, 2))
        self.assertFalse(g.remove_edge(0, 2))
        g = self.empty_graph_builder()
        self.assertFalse(g.remove_edge(0, 1))
        self.assertFalse(g.remove_edge(0, 2))

    def test_remove_node(self):
        g = self.empty_graph_builder()
        self.assertFalse(g.remove_node(0))
        self.assertFalse(g.remove_node(1))
        g = self.whole_graph_builder()
        self.assertTrue(g.remove_node(0))
        self.assertTrue(g.remove_node(1))
        g = self.specific_graph_builder()
        self.assertTrue(g.remove_node(5))
        self.assertFalse(g.remove_edge(5, 4))
        self.assertFalse(g.remove_edge(5, 6))
        self.assertTrue(g.remove_node(2))
        self.assertEqual(None, g.vertices_of_graph.get(2))
        self.assertFalse(g.remove_edge(0, 2))
        self.assertFalse(g.remove_edge(1, 2))

    def test_get_all_v(self):
        g = self.empty_graph_builder()
        self.assertEqual({}, g.get_all_v())
        g = self.no_edges_graph_builder()
        self.assertEqual(5, len(g.get_all_v()))
        self.assertTrue(0 in g.get_all_v().keys())
        self.assertTrue(4 in g.get_all_v().keys())
        self.assertFalse(6 in g.get_all_v().keys())
        g = self.specific_graph_builder()
        self.assertEqual(8, len(g.get_all_v()))
        self.assertTrue(0 in g.get_all_v().keys())
        self.assertTrue(4 in g.get_all_v().keys())
        self.assertFalse(11 in g.get_all_v().keys())
        self.assertFalse(12 in g.get_all_v().keys())

    def test_all_in_edges_of_node(self):
        g = self.no_edges_graph_builder()
        self.assertEqual({}, g.all_in_edges_of_node(0))
        self.assertEqual({}, g.all_in_edges_of_node(1))
        g = self.whole_graph_builder()
        self.assertEqual(5, len(g.all_in_edges_of_node(0)))
        self.assertEqual(5, len(g.all_in_edges_of_node(1)))
        self.assertEqual(5, len(g.all_in_edges_of_node(2)))
        g = self.specific_graph_builder()
        self.assertEqual(1, len(g.all_in_edges_of_node(1)))
        self.assertEqual(2, len(g.all_in_edges_of_node(2)))
        self.assertEqual(2, len(g.all_in_edges_of_node(6)))

    def test_all_out_edges_of_node(self):
        g = self.no_edges_graph_builder()
        self.assertEqual({}, g.all_out_edges_of_node(0))
        self.assertEqual({}, g.all_out_edges_of_node(1))
        g = self.whole_graph_builder()
        self.assertEqual(5, len(g.all_out_edges_of_node(0)))
        self.assertEqual(5, len(g.all_out_edges_of_node(1)))
        self.assertEqual(5, len(g.all_out_edges_of_node(2)))
        g = self.specific_graph_builder()
        self.assertEqual(2, len(g.all_out_edges_of_node(1)))
        self.assertEqual(1, len(g.all_out_edges_of_node(2)))
        self.assertEqual(2, len(g.all_out_edges_of_node(5)))
        self.assertEqual(1, len(g.all_out_edges_of_node(6)))


if __name__ == '__main__':
    unittest.main()
