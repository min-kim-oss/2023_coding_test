import sys
from collections import deque

com_num = int(sys.stdin.readline())
edge_num = int(sys.stdin.readline())
network = [[] for i in range(com_num+1)]

for i in range(edge_num):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

#print(network)

passed = []
queue = deque()

queue.append(1)
while(queue):
    now = queue.pop()
    if now not in passed:
        passed.append(now)
    for i in network[now]:
        if i not in passed:
            queue.append(i)
print(len(passed)-1)