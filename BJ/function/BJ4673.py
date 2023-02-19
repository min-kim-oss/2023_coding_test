d = [0 for i in range(0,10001)] 

for i in range(1, 10001):
    num = list(map(int,str(i)))
    sum = i
    for j in range(len(num)):
        sum += num[j]        
    if(sum <= 10000):
        d[sum] +=1
    
for i in range(1,10001):
    if(d[i] == 0):
        print(i)