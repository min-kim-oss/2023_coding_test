num = int(input())
i = 1
max_num = 1
while True:
    if(num <= max_num):
        print(i)
        break
    else:
        max_num += i*6
        i += 1