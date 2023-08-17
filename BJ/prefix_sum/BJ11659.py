import sys

n, m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

sum_arr = []
sum = 0
for i in range(n):
    sum += arr[i]
    sum_arr.append(sum)

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(sum_arr[end - 1] - 0)
    else:
        print(sum_arr[end - 1] - sum_arr[start - 2])