import sys

num = int(sys.stdin.readline())

arr = []

for i in range(num):    
    input_arr = list(sys.stdin.readline().strip().split())
    print(input_arr)
    if input_arr[0] == "push": 
        arr.append(input_arr[2])
        
    elif input_arr[0] == "pop":
        if(len(arr) == 0):
            print(-1)
        else:
            pop_num = arr.pop()
            print(int(pop_num))
    elif input_arr[0] == "size":
        print(len(arr))
        
    elif input_arr[0] == "empty":
        if(len(arr) == 0):
            print(1)
        else:
            print(0)
            
    elif input_arr[0] == "top":
        if(len(arr) == 0):
            print(-1)
        else:
            print(int(arr[len(arr)-1]))