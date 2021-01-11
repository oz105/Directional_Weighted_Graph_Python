# Directional_Weighted_Graph_Python


### Directed weighted graph is a graph that is made up of a set of vertices connected by edges, where the edges have a direction associated with them.



![alt text](https://i.stack.imgur.com/YC8LA.gif)






In this Project there is implemention of a directed weighted graph which functions such as add new node to the graph , set an edge between 2 nodes and give the edge weight checking what is the shorthest path between 2 nodes and more.

NodeData
This is a class implements the node_data interface and create a new type of object. In this class we created a new object named node_data that contains 
every node also contains an integer named tag and a double named weight (which will be used in the next classes), a String named info and a geo_location field named position that save the location of the node in a two dimension space.
In this class there are methods to update the tag, the info, the weight, to get a given node's key value, info, neib nodes and tag.

DiGraph
This class implements the interface GraphInterface, and create a new type of object. The graph is directed, which means that connection between two nodes isn't symmetric.
in this class there is one more class called NodeData In this class we created a new object each node data hold some variables 
each node have particular id -> there is no way there is 2 node data in the graph with the same id 
his pos -> (x,y,z)
the edges come out from him -> holds in a dictionary named out_edges the key is the dest node and the value is the weight of the edge between them.
and the edges come to him -> holds in a dictionary named in_edges the key is the src node and the value is the weight of the edge between them.
and there is "get_from" , "tag" , "weight" that will be used in the algorithms.

In DiGraph we used in dictionary named vertices_of_graph this dictionary holds all the node data of the graph i.e. holds the vertices of the graph.

### the methods we have in this Class are :
1. addNode - we need to give this method a key we want to add to the graph if there is such key will do nothing , add it otherwise.

2. add edge - we need to give 2 keys and weight and than it will make an edge between this keys and the weight of this edge will be the weight we put in.
  if one of the keys not in the graph will do nothing.
  
3. removeNode - we need to give this method a key and it will delete the node from the graph including all his edges ,come out from him and come to him 
4. removeEdge - we need to give this method 2 keys and it will remove the specific edge between them if there is no edge like this it will do noting.

5.get_all_v - we give nothing to this method and it will return to us a dictionary named vertices_of_graph that holds all the vertices of the graph the key is the id     of the node and the value is the node itself.

6.all_in_edges_of_node - we need to give this method a key and it will return dictionary of all the edges come to him in the key we will have the src node in the value   we will hold the weight of the edge.

7.all_out_edges_of_node - we need to give this method a key and it will return dictionary of all the edges come from him. in the key we will have the dest node in the   value we will hold the weight of the edge.

8. v_size - this method will return the number of the vertices in the graph .
9. e_size - this method will return the number of the edges in the graph .
10. get_mc - this method will return the number of the changes in the graph .
11. __eq__ -> equals - we need to give this method a DiGraph and it will return true if this graph and the graph we gave is the same . 




![alt text](https://www.researchgate.net/publication/337070671/figure/fig2/AS:865839351857152@1583443596094/An-example-of-directed-weighted-graph.png)




Graph_Algo
This class implements the interface GraphAlgoInterface, it creates a new type, that contains only a private graph named graph_algo.
This class contains methods that help the user to get information about the graph and about nodes and edges in it.


#### Kosaraju's algorithm

First of all, this is a method that didn't come from the interface, but if helps the method that the interface does contain. This method named kosarajus, it gets a int named start from the graph, and the method run on the graph from this node start 2 times. In the first time we will run over it by the direction of the edges and to every node we mange to get we save his id in  dictionary called "visited" and changed his value to "1" keep runnig until we succeeded run the all nodes we can reach to. Now we will run again the secound time , but in this run we will run on the oppsite direction of the edges because we want to check if there is a way to get to the node start from each node we get in the first run time. Again we have a dictionary called "oppsite_visited"  and evrey node we reach to we will change his value in the dictionary to "1" when we done we will take only the nodes that shows up in both dictionarys meaning in the list we will return only nodes that present in the dictionary called "oppsite_visited" and present in the dictionary called "visited". this method will help us to implements the method connected_component. 

#### Dijkstra algorithm

this method implements the Dijkstra algorithm.
in this method we will mark all the nodes as unvisited (Tag = 0 -> means unvisited)
and we will mark the weight of every node as infinity (Weight = Double.MAX_VALUE)
we will create a PriorityQueue that will be give Priority base on the smallest weight
During the algorithm for every node we will saved 3 things
his weight form the src node - this will be store in the weight
and from who he gets that weight - this will be store in the info (the key of the node)
and if we visit in some node - this will be store in the tag.
and when we first visit in some node (means his tag = 0 )
we add him to the PriorityQueue .
the algorithm ends when the PriorityQueue is empty .
In the end of the algorithm each node will hold 3 things
1.the smallest weight from src node - will be store in the weight.
2.from who he gets this weight - will be store in the Info.
3.if the node have been visited or not - will hold in the tag.



There is a method shortestPathDist that returns the smallest weight of path between two give nodes. It sends one of them to the Dijkstra algorithm, and return the tag of the other. If there is no path then the default number will be -1, because the bfs didn't reach that node.
The least method is shortestPath that returns a list of all the nodes between two given node's keys. If there are no nodes with those keys in the graph it returns null, if there is then if there is no path it would return an empty list, if they have a path if would send one to the bfs algorithm, and in a loop would start from the other node  and add every node that have the next number of tag- by that we go throw the other node, then the next in the graph, then the next until we reach the first node.

as we can see in the photo there is alot of ways between node 3 to node 11 but there is shoretes path.


![alt text](https://www.researchgate.net/profile/Trong_Do/publication/224234542/figure/fig2/AS:393713277784066@1470879968319/a-Weighted-directed-graph-topology-scenario-2.png)

