import time

from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


if __name__ == '__main__':
    start_time = time.time()
    algo = GraphAlgo()
    file = '../data/compere/G_10_80_1.json'
    algo.load_from_json(file)
    print(algo.shortest_path(1, 6))

    print(time.time() - start_time, "seconds")
