num = int(input())

for i in range(1,num+1):
    #print("check ")
    cur_num = i
    sum = cur_num
    while True:
        plus_num = cur_num % 10
        sum += plus_num
        if (cur_num // 10 == 0):
            break
        else:
            cur_num = cur_num // 10

    if sum == num:
        print(i)
        break
    elif i == num:
        print(0)