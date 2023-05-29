import sys

def checkSqr(arr, m , start_x, start_y):
#    print("in checkSqr", m)
    if m == 1: #한칸짜리 check시
        if (arr[start_x][start_y] == 1): #파란색이면
            return 0, 1
        else:                            #하얀색이면
            return 1, 0
    else:      #한칸짜리가 아닐시
        check_num = 0
        if (arr[start_x][start_y] == 1):
            check_num = 1
        for i in range(m):
            for j in range(m):
                if(arr[start_x + i][start_y + j] != check_num): #만약 check 한 상자가 같은 색이아니면
                    ul_white, ul_blue = checkSqr(arr, m//2 , start_x, start_y)
                    ur_white, ur_blue = checkSqr(arr, m//2 , start_x, start_y + m//2)
                    dl_white, dl_blue = checkSqr(arr, m//2 , start_x + m//2, start_y)
                    dr_white, dr_blue = checkSqr(arr, m//2 , start_x + m//2, start_y + m//2)
                    white = ul_white + ur_white + dl_white + dr_white
                    blue = ul_blue + ur_blue + dl_blue + dr_blue
                    return white, blue

        #check한 상자가 모두 같은 색이면
        if(check_num == 1): #파란색이면
            return 0, 1
        else:  # 하얀색이면   #하얀색이면
            return 1, 0


arr = []
m = int(sys.stdin.readline());
for i in range (m):
    arr.append(list(map(int, sys.stdin.readline().split())))
#print(arr)


white, blue = checkSqr(arr, m, 0 , 0)
print(white)
print(blue)


