import sys

height = int(sys.stdin.readline())

#print("height :", height)

table = []
for i in range(height+1):
    table.append([0 for i in range(height+1)])

#print("arr :")
#print(table)

students = {}#[[]]*(height*height+1)
#print(students)
for i in range(height*height):
    arr= list(map(int, sys.stdin.readline().split()))
    #print(arr)
    #arr = list(int(sys.stdin.readline().strip()))
    if len(arr[1:]) == 0:
        students[arr[0]] = [-1]
    else:
        students[arr[0]] = arr[1:]

print(students)
#print(len(students))
x = [0 ,1, 0 , -1]
y = [1 ,0, -1 , 0] #우 아래 좌 위 방향으로 확인





for cur_student, cur_values in  students.items(): #학생수만큼 탐색을 진행
    #print("cur_student : ", cur_student)
    #print("cur_values : ", cur_values)
    max_indexX = 0
    max_indexY = 0
    max_value = 0
    max_empty = 0
    for i in range(1,height+1):
        for j in range(1, height+1):
            #print("i, j : ", i, j)
            temp_value = 0
            temp_empty = 0

            if table[i][j] != 0:
                continue;

            for k in range(len(x)):
                check_indexX = i + x[k]
                check_indexY = j + y[k]
                if(height < check_indexX or check_indexX < 1):
                    continue
                if(height < check_indexY or check_indexY < 1):
                    continue

                if table[check_indexX][check_indexY] in cur_values:
                    temp_value += 1
                elif(table[check_indexX][check_indexY] == 0):
                    #print("check i, j : ", check_indexX,check_indexY )
                    temp_empty += 1

            if temp_value > max_value:
                #print("change1 i, j : ", i, j)
                max_indexX = i
                max_indexY = j
                max_value = temp_value
                max_empty = temp_empty
            elif temp_value == max_value:
                if temp_empty > max_empty:
                    #print("change2 i, j : ", i, j)
                    #print("max empty: ",max_empty)
                    #print("cur empty: ",temp_empty)
                    max_indexX = i
                    max_indexY = j
                    max_value = temp_value
                    max_empty = temp_empty

    table[max_indexX][max_indexY] = cur_student
    #print(table)
print(table)

total_value = 0

for i in range(1, height + 1):
    for j in range(1, height + 1):
        print(table[i][j])
        cur_values = students[table[i][j]]
        #print("cur_values :", cur_values)
        temp_value = 0
        for k in range(len(x)):
            check_indexX = i + x[k]
            check_indexY = j + y[k]
            if (height < check_indexX or check_indexX < 1):
                continue
            if (height < check_indexY or check_indexY < 1):
                continue

            if table[check_indexX][check_indexY] in cur_values:
                # print("check value")
                temp_value += 1
        if temp_value == 1:
            total_value += 1
        elif temp_value == 2:
            total_value += 10
        elif temp_value == 3:
            total_value += 100
        elif temp_value == 4:
            total_value += 1000
print(total_value)