# -*- CODING: UTF-8 -*-

arr = []

for i in range(9):
    arr.append(list(map(int,input().split())))     

max = 0
max_row = 0
max_column = 0

for i in range(9):
    for j in range(9):
        if(max < arr[i][j]):
            max = arr[i][j]
            max_row = i
            max_column = j

print(max)
print(max_row+1, max_column+1)