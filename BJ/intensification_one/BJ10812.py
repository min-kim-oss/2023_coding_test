bag_num, rotate = map(int, input().split())

bag = []

for i in range(0, bag_num+1):
    bag.append(i)


for i in range(rotate):
    begin , end, mid = map(int, input().split())
    arr = []
    for j in range(end - mid + 1):
        arr.append(bag[j + mid])
    for j in range(mid - begin):
        arr.append(bag[j + begin])
    for j in range(end- begin + 1):
        bag[j + begin] = arr[j]
for i in range(1, bag_num+1):
    print(bag[i], end= " ")