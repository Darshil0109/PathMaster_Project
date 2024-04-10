import numpy as np
infinity=float('inf')
a=np.array([[0,8,5],[2,0,infinity],[infinity,1,0]])
count=0
temp=[[0,8,5],[2,0,infinity],[infinity,1,0]]
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

starting_node=65
for i in range(len(a)):
    for j in range(len(a)):
        if (i!=j):
            print(f"From Node {chr(starting_node+i)} to Node {chr(starting_node+j)} ",a[i][j])