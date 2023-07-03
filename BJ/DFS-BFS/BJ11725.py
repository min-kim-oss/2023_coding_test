"""

import sys

num = int(sys.stdin.readline())
#print("num:" ,num)

arr = []

for i in range(num):
    arr.append(list(map(int,sys.stdin.readline().split())))
#print("arr: ", arr)

node = [False for i in range(num+1)]
parent = [1 for i in range(num+1)]
#print("node", node)
#print("parent", parent)

next = []
next.append(1)

while(len(next) != 0):
    now = next.pop(0)
#    print(now)
    node[now] = True
    for i in range(len(arr)):
        if ( now in arr[i] ):
            if (now == arr[i][0]) and (node[arr[i][1]] != True):
                next.append(arr[i][1])
                parent[arr[i][1]] = now
            elif (now == arr[i][1]) and (node[arr[i][0]] != True):
                next.append(arr[i][0])
                parent[arr[i][0]] = now

#print("ans")
for i in range(2, len(parent)):
    print(parent[i])

"""

import sys

num = int(sys.stdin.readline())
#print("num:" ,num)



graph = [[] for i in range(num+1)]
#print("graph", graph)

for i in range(num-1):
    new = list(map(int,sys.stdin.readline().split()))
#    print("new:", new)
    graph[new[0]].append(new[1])
    graph[new[1]].append(new[0])

#print(graph)

node = [False for i in range(num+1)]
parent = [1 for i in range(num+1)]
#print("node", node)
#print("parent", parent)

next = []
next.append(1)

while(len(next) != 0):
    now = next.pop(0)
#    print(now)
    node[now] = True
    for i in graph[now]:
        if node[i] != True:
            next.append(i)
            parent[i] = now

#print("ans")
for i in range(2, len(parent)):
    print(parent[i])