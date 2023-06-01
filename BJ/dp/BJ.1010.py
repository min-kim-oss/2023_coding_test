import sys

def pactorial(n):
    count = 1
    for i in range(n, 0 ,-1):
        count *= i
    return count


test_case = int(sys.stdin.readline())

for i in range(test_case):
    n, m = map(int, sys.stdin.readline().split())

    ans = 1
    for i in range(m, 0 , -1):
        if (i == (m-n)):
            break
        ans *= i
    ans //= pactorial(n)
    print(ans)