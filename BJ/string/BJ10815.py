n = int(input())
card_list = list(map (int,(input().split())))
m = int(input())
check_list = list(map (int,(input().split())))

dic = {}

for i in range (n):
    dic[card_list[i]] = 0

for i in range(m):
    if check_list[i] in dic.keys():
        print(1, end = " ")
    else:
        print(0, end=" ")




