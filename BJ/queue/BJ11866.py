n,  k = map(int,input().split())

circle_arr = [i for i in range(1, n+1)]
#print(circle_arr)
out_arr = []

num = 0
while True:
    num += k
    if num > len(circle_arr):
        num = (num % len(circle_arr)) 
        #print("check")
    #for check
    #print("--------")
    #print("len : " , len(circle_arr))
    #print("delete : ",num)
    out_arr.append(circle_arr[num-1])
    #print("del_num : ", circle_arr[num-1])
    del circle_arr[num-1]
    if(len(circle_arr) == 0):
        break
    if num - 1 <= 0:
        num = len(circle_arr)
    else:
        num -= 1
    #print("after delete : ",num)
    #print(circle_arr)
    #print("--------")

print("<", end ="")
for i in range(len(out_arr)):
    if (i != (len(out_arr)-1)):
        print(out_arr[i], end = ", ")
    else:
        print(out_arr[i], end = "")
print(">", end ="")