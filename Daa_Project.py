import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
g = nx.DiGraph()
infinity=float('inf')
a=np.array([[0,8,5],[2,0,infinity],[infinity,1,0]])
# a=np.array([[0, 3, infinity, 7], [1, 0, 6, infinity], [infinity, 3, 0, 7], [7, infinity, 3, 0]])
count=0
temp=a.tolist()
starting_node=65
for i1 in range(len(a)):
    for j1 in range(len(a[i1])):
        # Infinite weight shows that there is no edge between two edges
        # draw edges that don't have infinite value 
        if a[i1][j1]!=infinity:
            g.add_edge(chr(starting_node+i1),chr(starting_node+j1),weight=a[i1][j1])

# Floyd Warshell's Algorithm
for w in range(len(a)):
    if count!=len(a):
        count+=1
    for i in range(len(a)):
        for j in range(len(a)):
            #print(f"a[{i}][{count-1}] + a[{count-1}][{j}]",a[i][count-1] + a[count-1][j])
            temp[i][j]=min(a[i][j],(a[i][count-1] + a[count-1][j]))
            #print(f"temp[{i}][{j}]",temp[i][j])
        a=temp
     #print('Temp',temp)    #to see after each iteration change in Given input

#print('a',a)

# To print Output in Terminal
for i in range(len(a)):
    for j in range(len(a)):
        if (i!=j):
            print(f"From Node {chr(starting_node+i)} to Node {chr(starting_node+j)} ",a[i][j])

# To position All Nodes in Circle 
pos=nx.circular_layout(g)
# Get weight of all edges
labels = nx.get_edge_attributes(g,'weight')
# to draw edges and labels
nx.draw(g, pos, connectionstyle='arc3,rad=0.1' ,with_labels=True)
# to draw edge's weights 
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels,connectionstyle='arc3, rad = 0.1')
plt.show()