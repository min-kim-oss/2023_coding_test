test_case = int(input())

for i in range (test_case):
    height, weight, num = map(int, input().split())
    room_num = num // height + 1
    room_floor = num % height
    if(room_floor == 0):
        room_num -= 1
        room_floor = height
    room_num = room_num + 100 * room_floor
    print(room_num)
