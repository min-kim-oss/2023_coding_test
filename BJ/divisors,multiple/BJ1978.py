num = int(input())
num_arr = list(map(int, input().split()))

count = num

for i in range(num):
    if (num_arr[i] == 1):
        count -= 1
        continue
    for j in range(2, num_arr[i]):
        if(num_arr[i] % j == 0):
            count -= 1
            break
print(count)







