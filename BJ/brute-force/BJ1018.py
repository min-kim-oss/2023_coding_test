height, width = map(int, input().split())

board = []

for i in range(height):
    board.append(list(input()))

lowest = 64

for i in range(height - 8 + 1):
    for j in range (width - 8 + 1):
        start = board[i][j]
        change = 0
        #print(i, j)
        for k in range(8):
            for l in range(8):
                if(k == 0 and l == 0): #체스판의 [0][0]인 부분은 판단 x이기에 스킵한다.
                    continue
                elif((k + l) % 2 == 0): #체스판에서 [0][0] 인 부분과 같은 색이어야 하는 부분 판단
                    if (board[i+k][j+l] != start):
                        change +=1
                else:
                    if((board[i+k][j+l] == start)):
                        change +=1
        if (change < lowest):
            lowest = change

        change = 1 #[0][0] 을 뒤집는 경우가 너 적은 경우가 나올수 있기에 확인작업
        for k in range(8):
            for l in range(8):
                if(k == 0 and l == 0): #체스판의 [0][0]인 부분은 판단 x이기에 스킵한다.
                    continue
                elif((k + l) % 2 == 0): #체스판에서 [0][0] 인 부분과 같은 색이어야 하는 부분 판단
                    if (board[i+k][j+l] == start):
                        change +=1
                else:
                    if((board[i+k][j+l] != start)):
                        change +=1
        if (change < lowest):
            lowest = change

print(lowest)