d = [0 for i in range(30)]
for i in range(28):
    num = int(input())
    d[num-1] = 1
for i in range(30):
    if(d[i]==0):
        print(i+1)