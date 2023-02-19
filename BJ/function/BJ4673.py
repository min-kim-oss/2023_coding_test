d = [0 for i in range(0,10001)] 

for i in range(1, 10001):
    num = list(map(int,str(i)))
    sum = i

    #---logical solution---
    m = i
    while(True):
        if m ==0 :
            break
        sum += (m%10)
        m /= 10
        m = int(m)
    if(sum <= 10000):
        d[sum] +=1

    #--- python function ---
    # for j in range(len(num)):
    #     sum += num[j]        
    # if(sum <= 10000):
    #     d[sum] +=1
    
for i in range(1,10001):
    if(d[i] == 0):
        print(i)