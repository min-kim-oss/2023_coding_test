num = int(input())
d = input().split()
max = int(d[0])

for i in range(num):
    if(max < int(d[i])):
        max = int(d[i])

sum = 0

for i in range(num):
    sum += int(d[i])/max * 100

print(sum/num)