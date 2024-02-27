import sys
from collections import deque

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.reverse()

dq = deque()
for i in range(N): #0부터
    if li[i] == 1:
        dq.appendleft(i + 1) #1
    elif li[i] == 2:
        dq.insert(1, i + 1)
    elif li[i] == 3:
        dq.append(i + 1)
    # print(dq)

for i in dq:
    print(i, end=" ")