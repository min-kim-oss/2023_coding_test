row , column = map(int, input().split()) 
arr_a = []
arr_b = []
for i in range(row):
    arr_a.append(list(map(int,input().split())))        

for i in range(row):
    arr_b.append(list(map(int,input().split()))) 
    
for i in range(row):
    for j in range(column):
        print(arr_a[i][j] + arr_b[i][j], end = " ")
    print()