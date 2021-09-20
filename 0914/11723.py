import sys
import heapq

n =int(sys.stdin.readline())
h = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(h, (abs(num), num))
    else:
        try:
            print(heapq.heappop(h)[1])
        except:
            print(0)