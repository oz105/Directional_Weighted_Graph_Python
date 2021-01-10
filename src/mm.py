import queue

from src.DiGraph import DiGraph

if __name__ == '__main__':

   dict = {1: 8, 2: 9, 3: 5}
   print(3 in dict)
   print(dict)


   q = queue.Queue()
   q.put(90)
   q.put(5)
   #q.get(0)
   print(" dnns", q.get(7))
