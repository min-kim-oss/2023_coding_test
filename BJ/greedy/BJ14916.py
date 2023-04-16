money_change = int(input())
# print(money_change)

five_num =money_change//5
left_money_change = money_change % 5
# print(five_num, money_change)

if ((left_money_change % 2) != 0):
    five_num -= 1
    left_money_change += 5
    if(left_money_change > money_change):
        print(-1)
    else:
        two_num = left_money_change // 2
        print(five_num + two_num)

else:
    two_num = left_money_change // 2
    print(five_num + two_num)




