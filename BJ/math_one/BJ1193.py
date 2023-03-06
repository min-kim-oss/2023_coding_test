num = int(input())
up = 1
down = 1
max = 1
count = 1
befo_count = 0
add_num = 1
way = 1 #1 is going up -1 is going down
while (num >= befo_count + add_num + 1):
    befo_count = count
    add_num += 1
    count += (add_num)
    max += 1


if add_num % 2 == 0:
    way = -1
else:
    way = 1
if way == 1:
    up = max - (num - befo_count - 1)
    down = 1 + (num - befo_count - 1)

else:
    up = 1 + (num - befo_count - 1)
    down = max - (num - befo_count - 1)


print(up , "/", down , sep ="")
