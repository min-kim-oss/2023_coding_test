import sys

arr = list(sys.stdin.readline().strip())
# print(arr)


AAAA_mask = 4
BB_mask = 2
check = 0

# for i in range(10, 6, -1):
#     print(i)
for now in range(len(arr)):

    if(arr[now] == 'X'):
        check += 1
        # print("check : ", check)
    elif(arr[now] == '.'):
        if ( check == 4 ):
            for i in range(now-1,now-1-4,-1):
                # print("change: ", i)
                arr[i] = 'A'
        if ( check == 2 ):
            for i in range(now-1, now-1-2, -1):
                # print("change: ", i)
                arr[i] = 'B'
        check = 0
    if check == 4:
        for i in range(now, now - 4, -1):
            # print("change: ", i)
            arr[i] = 'A'
        check = 0
    if (check == 2) and ( now + 1 == len(arr)):
        for i in range(now , now-2, -1):
            # print("change: ", i)
            arr[i] = 'B'

check_test = True
for i in range(len(arr)):
    if arr[i] == 'X':
        check_test = False
        break
if check_test:
    for i in range(len(arr)):
        print(arr[i],end="")
else:
    print(-1)