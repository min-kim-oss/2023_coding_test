a, b, v = map(int,input().split())

days = 0
height = 0

for i in range(a, 0 , -1):
    #print (i)
    if ((v - i) % (a - b) == 0):
        days = (v - i) / (a - b) + 1
        break

print(int(days))