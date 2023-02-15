a = int(input())
b = input().split()
c = int(input())

for i in range(a):
    b[i] = int(b[i])

count = 0

for i in range(a):
    if b[i] == c:
        count += 1

print(count)