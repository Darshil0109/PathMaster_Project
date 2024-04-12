import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import itertools
class FloydWarshallAlgo:
    def __init__(self,a):
        self.a=a
# for Directed Graph 
    def FloydAlgo(self):
        g = nx.DiGraph()
        g1=nx.DiGraph()
        count=0
        temp=self.a.tolist()
        starting_node=65    #for ascii code to print Node A, B ,C ,...
        # to set window size which shows graph
        plt.rcParams["figure.figsize"] = (12, 6)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('Input Graph')
        ax2.set_title('Minimum path to Explore to all Nodes')
        for i1 in range(len(a)):
            for j1 in range(len(a[i1])):
                # Infinite weight shows that there is no edge between two edges
                # draw edges that don't have infinite value 
                if self.a[i1][j1]!=infinity:
                    g.add_edge(chr(starting_node+i1),chr(starting_node+j1),weight=self.a[i1][j1])

        # Floyd Warshell's Algorithm
        for w in range(len(self.a)):
            if count!=len(self.a):
                count+=1
            for i in range(len(self.a)):
                for j in range(len(self.a)):
                    #print(f"a[{i}][{count-1}] + a[{count-1}][{j}]",a[i][count-1] + a[count-1][j])
                    temp[i][j]=min(self.a[i][j],(self.a[i][count-1] + self.a[count-1][j]))
                    #print(f"temp[{i}][{j}]",temp[i][j])
                self.a=temp
            #print('Temp',temp)    #to see after each iteration change in Given input

        #print('a',a)

        # To print Output in Terminal
        for i in range(len(self.a)):
            for j in range(len(self.a)):
                if (i!=j):
                    print(f"From Node {chr(starting_node+i)} to Node {chr(starting_node+j)} ",self.a[i][j])

        # To position All Nodes in Circle 
        pos=nx.circular_layout(g)
        # Get weight of all edges
        labels = nx.get_edge_attributes(g,'weight')
        # to draw edges and labels
        nx.draw(g, pos, connectionstyle='arc3,rad=0.1' ,with_labels=True,ax=ax1)
        # to draw edge's weights 
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels,connectionstyle='arc3, rad = 0.1',ax=ax1)


        path=[]
        input_range=list(range(0,len(a)))
        # generates combination of different Ways like [1,2,3,4],[4,3,2,1],[1,3,2,4],etc....
        path_combinations=[list(perm) for perm in itertools.permutations(input_range)]
        # print(path_combinations)         #to see all ways to explore path

        # Calculate that how much time each path would take and store it in path list
        for i in range (len(path_combinations)):
            path_value=0
            for j in range(len(path_combinations[i])-1):
                val1=path_combinations[i][j]
                val2=path_combinations[i][j+1]
                path_value+=a[val1][val2]
            path.append(path_value)
        # print(path)                       #to print time for each path combination
        # get index of minimum time from path list and get combination of path at that index 
        min_path=path_combinations[path.index(min(path))]

        # Draw Minimmum path in second subplot
        for i in range(len(min_path)-1):
            # suppose if min_path=[3,2,1] then val1=3 , val2=2 for first iteraation
            val1=min_path[i]
            val2=min_path[i+1]
            g1.add_edge(chr(starting_node+val1),chr(starting_node+val2),weight=a[val1][val2])
        g1.in_degree('A')
        # to draww second graph
        pos1=nx.circular_layout(g1) 
        labels1=nx.get_edge_attributes(g1,'weight')
        nx.draw(g1, pos1, connectionstyle='arc3,rad=0.1' ,with_labels=True,ax=ax2)
        nx.draw_networkx_edge_labels(g1,pos1,edge_labels=labels1,connectionstyle='arc3, rad = 0.1',ax=ax2)
        plt.tight_layout()
        plt.show()

infinity=float('inf')
# self.a=np.array([[0,8,5],[2,0,infinity],[infinity,1,0]])
a=np.array([[0, 3, infinity, 7], [1, 0, 6, infinity], [infinity, 3, 0, 7], [7, infinity, 3, 0]])
obj=FloydWarshallAlgo(a)
obj.FloydAlgo()
