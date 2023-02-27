num = int(input())

for i in range(1,num+1):
    #print(i)
    for j in range(num-i):
        print(" ",end="")
    for j in range(i*2 - 1):
        print("*",end="")
    print()
for i in range(num-1,0,-1):
    #print(i)
    for j in range(num-i):
        print(" ", end="")
    for j in range(i*2 - 1):
        print("*", end="")
    print()