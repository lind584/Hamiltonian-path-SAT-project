# Hamiltonian path SAT project
# Documentation
## Problem description
A graph contains a Hamiltonian path if and only if it has a path which connects all the vertices. Therefore, we need to tell if a graph has a Hamiltonian path or not. We have an input graph: This includes the information about which edges of the graph are present in such graph based on which vertices connect them. The graph is going to be directed.
We need to encode it in a CNF formula. Every vertex needs to be visited exactly once in order for a H. path to exist. It is known that this problem is NP-complete.
### Input
N = number of vertices of the graph on the first line
For each line after that, an edge oriented from ith to jth vertex.
An example of a valid input:
```
4
1 2
2 3
3 4
```
This graph contains a Hamiltonian path. The correct output is:
```
true
```

TODO:
## Encoding
## User documentation
## Example instances
(what is in the instances folder)
## Experiments