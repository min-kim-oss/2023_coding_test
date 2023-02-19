a = int(input())
b = list(map(int,input()))
sum = 0
for i in range(a):
    sum += b[i]
print(sum)