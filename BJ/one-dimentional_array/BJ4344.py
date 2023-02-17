num = int(input())

for i in range(num):
    d = input().split()
    sum = 0
    for j in range(1,len(d)):
        sum += int(d[j])

    avg = sum/int(d[0])

    count = 0
    for j in range(1,len(d)):
        if(int(d[j]) > avg):
            count+=1

    print("{0:.3f}".format(count/int(d[0])*100),"%",sep="")