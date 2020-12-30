import unittest
from random import random

from src.main import NodeData, EdgeData, DiGraph

class GraphTests:


    def nextRnd(self, min = 0, max = 100):
        seed = 30
        d = random(seed).nextDouble();
        dx = max - min;
        ans = d * dx + min;
        return ans;



    def testNodeGetKey(self):
        key = self.nextRnd(0, 5)
        n = NodeData(key)
        self.assertEqual(key, n.getKey)




