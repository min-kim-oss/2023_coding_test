d = []
max = 0
order_num =0
for i in range(9):
    num = int(input())
    d.append(num)
    # if( i == 0 ):
    #     max = int(d[i])
    #     order_num = i
    # else:
    if(max < int(d[i])):
        max = int(d[i])
        order_num = i
print(max)
print(order_num+1)