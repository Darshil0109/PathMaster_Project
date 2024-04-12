import numpy as np
import Dijkstra as DK
import FloydWarshall as FW
infinity=float('inf')
print("[1] . Find Way from One Node to Each & Every Other Nodes. [Dijkstra's Algo.]")
print("[2] . Find Way from Each Nodes to Every Other Nodes. [Floyd Warshall Algo.]")
choice=int(input("Enter Your Choice: "))
if choice==1:
    obj=DK.DijkstraSolver()
    obj.main()
elif choice==2:
    n=int(input("Enter No. of Nodes: "))
    temp_l=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                temp_l.append(0)
            else:
                temp_input=input(f"Enter Distance Between Node {chr(65+i)} and Node {chr(65+j)} (If there is No Way between These node write infinity): ")
                if temp_input=="infinity":
                    temp_l.append(infinity)
                else:
                    temp_l.append(int(temp_input))
    input_graph=np.array(temp_l)
    input_graph=input_graph.reshape(n,n)
    print(input_graph)
    obj=FW.FloydWarshallAlgo(input_graph)
    obj.FloydAlgo()
else:
    print("Wrong Choice: ")