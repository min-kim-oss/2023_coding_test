node, edge, start = map(int,input().split())
#print(node, edge, start)
edges = []
for i in range(edge):
    edges.append(list(map(int,input().split())))




DFS = []
order = []
state_edge = sorted(edges)

state = start
order.append(state)

end = 0

while(True):
    for i in range(len(state_edge)):
        if( state_edge[i][0] == state ):
            if(state_edge[i][1] not in order):
                DFS.append(state_edge[i])
                state_edge.pop(i)
                break
        elif( state_edge[i][1] == state ):
            if (state_edge[i][0] not in order):
                DFS.append(state_edge[i])
                state_edge.pop(i)
                break

    if (DFS[len(DFS)-1][0] == state):
        order.append(DFS[len(DFS)-1][1])
        state = DFS[len(DFS)-1][1]
    elif(DFS[len(DFS)-1][1] == state):
        order.append(DFS[len(DFS)-1][0])
        state = DFS[len(DFS)-1][0]

    if(len(order) == node):
        break
for i in range(node):
    print(order[i], end = " ")
print()

BFS = []
order = []
state_edge = sorted(edges)
state = start
state_index = 0
order.append(state)


while(True):
    for i in range(len(state_edge)):
        if (state_edge[i][0] == state):
            BFS.append(state_edge[i])
        elif (state_edge[i][1] == state):
            BFS.append(state_edge[i])



    for i in range(len(BFS)):
        if (BFS[i][0] == state):
            if(BFS[i][1] not in order):
                order.append(BFS[i][1])

        elif (BFS[i][1] == state):
            if(BFS[i][0] not in order):
                order.append(BFS[i][0])


    state_index += 1
    state = order[state_index]
    if (len(order) == node):
        break
for i in range(node):
    print(order[i], end=" ")
print()


