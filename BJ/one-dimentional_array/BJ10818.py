n = int(input())
d = input().split()

max = int(d[0])
min = int(d[0])

for i in range(n):
    if int(d[i]) > max:
        max = int(d[i])
    elif int(d[i]) < min:
        min = int(d[i])
print(min  , max)