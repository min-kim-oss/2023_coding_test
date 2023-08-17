import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

sum = sum(arr)
total = 0

for i in range(n-1):
    # print("print",arr[i])
    sum -= arr[i]
    total += ((sum)*arr[i])
print(total)