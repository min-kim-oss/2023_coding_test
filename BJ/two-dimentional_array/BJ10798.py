# -*- CODING: UTF-8 -*-

arr = []
for i in range(5):
    arr.append([])
    for j in range(15):
        arr[i].append(-1)
        


for i in range(5):

    temp_arr=(list(str(input())))
    
    for j in range(len(temp_arr)):
        arr[i][j] = temp_arr[j]
        

for i in range(15):
    for j in range(5):
        if(arr[j][i] != -1):
            print(arr[j][i], end = "")