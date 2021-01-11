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
The new type contains HashMap named verticesOfGraph, of node_data as value and integer as key, which holds within in all the node_datas that that graph holds, while creating a new graph the class initialized the HashMap to be empty.
Another HashMap named edgesOfGraph than contains a node_data as the key and another HashMap as a value, that contains a node_data as a key and edge_data as a value. It represents all the edges between two node_datas.
There is a HashMap named reverse that contains all the reverse edges which used in the next class to get all the edges that come in a given node.
There ar two integers one named edgeSize that count the number of edges in the graph, the second named changesNum which keeps track about the number of changes that the graph has been through. While creating a new graph both of these counters are given the value 0.
All of the implements are private, and there is a option to get their value, if we try to get all of the node_datas in the graph we will get a collection of node_datas.
There is a constructor to the graph, a copy constructer (which get a graph to copy from, named copyG, and a graph to copy into).
There is a method named getNode, that while given a key value, checks first if there is a node_data that contains that key- if not than it returns null, and if the graph contains a node_data with that key, than it gets it from the HashMap verticesOfGraph and return it.
There is an methods to addnode_data to the graph, while given a node_data, in this method we first check if the graph didn't have a node_data like this, if it has than we don't add it to avoid duplication. 
There is a method that receive two integers named src and dest, that edge connect between two node_datas if there are two node_data with the key values that were given. To connect between two node_datas we use the method connect in the node_data class.
There is a getV method that returns a collection of node_datas that the graph contains. There is other method with the same name that gets an integer named key, first the method checks if the graph contains a node_data with that key, if not than it returns null, if it contains it then it returns all of this node_data neib collection, using the method getNi from node_data.
Other method named removeNode gets a key value, we use the method get from node_data class to get the node we want to remove, and save it. By using foreach it passes through all of that node neighbors'' and remove it from edgesOfGraph and revers, the method does it by using the removeNode. At the end we remove that node from the HashMap verticesOfGraph of the graph, and return the removed node. If the node doesn't exist then we return null because there is nothing to remove.
There is also a method that remove an edge between two node_datas, given two integers. First, we check if they even exist- if not we return null, if they do than we check if there is a connection between them to separate, if there is than by using the removeNode from the node_data class we remove one from the other's neib HashMap.
There are also methods named nodeSize, that returns the number of node_datas in allNodes, edgeSize that return the counter edgeSize and getMC that returns the counter modeCount. There us a method that returns the number of nodes in the graph, that called nodeSize, and it returns the number of values in the verticesOfGraph HashMap.


![alt text](https://www.researchgate.net/publication/337070671/figure/fig2/AS:865839351857152@1583443596094/An-example-of-directed-weighted-graph.png)

Graph_Algo
This class implements the interface dw_graph_algorithms, it creates a new type, that contains only a private graph named gAlgo.
This class contains methods that help the user to get information about the graph and about nodes and edges in it.
There are contractors of empty graphAlgo that is empty, there is a copy constructure that do a deep copy, and there is the init copy that do a shallow copy of the graphs.

#### BFS 2 Ways 

First of all, there is a method that didn't come from the interface, but if helps the method that the interface does contain. This boolean method named bfs, it gets a node named node from the graph, first we change all of the tags of the nodes in the graph to -1. Then, by using a queue named q, we change the tag of every node we get to 1, very time the bfs changes a node's tag is add it to the q. We start with the original node, put it in the q and that start a loop going throw all of his neighbors and set their tag to be 1, adding them to the q, we keep a counter that represent the number of nodes we have seen so far. At the end of the original node neighbors, we take him out of the q, and start going throw the next node in the q's neighbors. We do so again and again, count the nodes we have seen until the q is empty, then we know we have reached every node possible.
If the counter equals to the number of nodes in the graph than we found a node that has path to every other node in the graph, and the tags of all the nodes are 1.
Then the bfs restart the counter and the q, and it do all the process again only this time he go through all the reverse edges in the graph and count all the nodes we have seen so far, this time the tag will change to 2. 
By that we check if there's a path from every node in the graph to the given node, and path from him to every other node.
Then the bfs algorithm ends and return true if the counter equals to the number of nodes in the graph.
There is a Boolean method that checks if the g of this GraphAlgo is connected. This method uses the bfs algorithm by sending a random node. If the bfs return true if the graph, and false if it's not.

#### Dijkstra 

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

