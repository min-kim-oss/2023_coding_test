height, width = map(int,input().split())

map = []
for i in range(height):
    map.append(list(input()))


state_x = 0
state_y = 0
bfs = [[state_y,state_x]]
count = 0
end = 0

while end != 1:
    for_num = len(bfs)
    for i in range(for_num):
        state_y = bfs[0][0]
        state_x = bfs[0][1]
        #print("state : ", state_y, state_x)

        map[state_y][state_x] = '0'
        if(( state_x == width - 1 ) and (state_y == height -1)):
            print(count+1)
            end = 1
            break

        if (state_x + 1 < width ) and (map[state_y][state_x+1] == '1'):
            bfs.append([state_y,state_x+1])
        if (state_y + 1 < height ) and (map[state_y+1][state_x] == '1'):
            bfs.append([state_y+1, state_x])
        if (state_x - 1 >= 0) and (map[state_y][state_x-1] == '1'):
            bfs.append([state_y, state_x-1])
        if (state_y - 1  >= 0) and (map[state_y-1][state_x] == '1'):
            bfs.append([state_y-1, state_x])
        bfs.pop(0)

    count+=1
