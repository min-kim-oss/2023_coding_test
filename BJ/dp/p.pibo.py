import sys


def solution(n):
    piboArr = [0 for i in range(n + 1)]
    piboArr[0] = 0
    piboArr[1] = 1
    for i in range(2, n + 1):
        piboArr[i] = piboArr[i - 1] + piboArr[i - 2]

    answer = piboArr[n] % 1234567
    return answer


n = int(input())
answer = solution(n)
print(answer)