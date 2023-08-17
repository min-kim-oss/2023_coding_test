import sys

a,b, c, m = map(int, sys.stdin.readline().split())
# print(a,b,c,m)

work = 0
tired = 0

for i in range(24):
    if (tired + a <= m):
        work += b
        tired += a
    else:
        if(tired - c >= 0):
            tired -= c
        else:
            tired = 0

print(work)