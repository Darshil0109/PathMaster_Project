
# Pathmaster: Efficient PathFinder



Introducing a Python-based Design & Analysis of Algorithms(DAA) Project which is used to find distance to any node to  any other node using GUI visualization

We Have Mainly used 2 Algorithms:

[1]. Dijkstra's Shortest Path Algorithm[ Click Here ](https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php) 

[2]. Floyd warshall's Shortest Path Algorithm [ Click Here](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)


We have Used GUI visualization For Floyd Warshall Algorithm using Library Named [NetworkX](https://networkx.org/documentation/stable/index.html) 
## Installation

Install NetworkX Library using pip

```bash
  pip install networkx
```
    
Install MatPlotlib Library using pip

```bash
  pip install matplotlib
```
    
Install Numpy Library using pip

```bash
  pip install numpy
```
    
## Acknowledgements

 - [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html)



## Features

- Graphic User Interface (GUI)
- Graph Visualization & Analysis
- Efficient Path Finder
- Cross platform
- Design and Analysis of Algorithm


## Authors

- [@Darshil0109](https://github.com/Darshil0109)
- [@Deepshah2804](https://github.com/Deepshah2804)
- [@Hensypatel](https://github.com/Hensypatel)
- [@KshamtaShah](https://github.com/KshamtaShah)
- [@prachithacker24](https://github.com/prachithacker24)


## References

- Lok Jagruti Institute of Enginneering and Technology.

## Screenshots

![image](https://github.com/Darshil0109/Daa_project/assets/122811740/038ea173-b6ac-4187-a604-2a2553a99408)



## Lessons Learned

- GUI Development with NetworkX
- Shortest Path Logic
- Analysis of Graphs


## FAQ

#### 1. Can I visualize the results of these algorithms on a graph?

Absolutely You can visualize graph in Floyd Warshall algorithm and in Dijkstra's algorithm you can check in terminal where you run the code. Also, you can see shortest distance between 2 Nodes in floyd warshall in terminal

#### 2. Are there any practical applications of these algorithms?

Yes, Dijkstra's and Floyd-Warshall algorithms are widely used in various applications such as network routing protocols, GPS navigation systems, airline scheduling, and optimization problems in transportation and logistics.

#### 3.Why does the graph exploration process (2nd Graph) consider paths other than the shortest ones, even when multiple shortest paths exist between various pairs of nodes?

During graph exploration, the algorithm's objective is to identify the shortest paths between all pairs of nodes within the graph, not just between specific nodes like A and C or B and C.

#### 4. What is the time complexity of the project involving the implementation of Dijkstra's and Floyd-Warshall algorithms?

Since Dijkstra's algorithm has a time complexity of O(n^2) and Floyd-Warshall algorithm has a time complexity of O(n^3), the total time complexity of the project would be O(n^3). Also there is no Extra Loop used while taking input so time complexity won't change.
