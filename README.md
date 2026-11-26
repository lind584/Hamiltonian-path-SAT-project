# Hamiltonian path SAT project
# Hamiltonian path
A graph contains a Hamiltonian path if and only if it has a path which connects all the vertices. Therefore, we need to tell if a graph has a Hamiltonian path or not. We have an input graph: This includes the information about which edges of the graph are present in such graph based on which vertices connect them. The graph is going to be directed.
We need to encode it in a CNF formula. Every vertex needs to be visited exactly once in order for a H. path to exist. It is known that this problem is NP-complete.
On the input, we could have:
number of vertices of the graph on the first line
and for each vertex, a list of adjacent vertices which are connected by an edge to the given vertex
like so:
```
4
2
3
4
1
```
We have a Hamiltonian circuit in such graph, therfore we have a Hamiltonian path. The output should be true.
(One (start) vertex can be visited twice when it comes to H. circuits, fix example)