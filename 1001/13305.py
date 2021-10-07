from sys import stdin
import itertools
import sys

n = int(sys.stdin.readline())
distance=list(map(int, sys.stdin.readline().split()))
price=list(map(int, sys.stdin.readline().split()))

td=sum(distance)
now=price[0]*distance[0]
for p in range(1,n-1):
    if(price[p]>price[p-1]):
        now+=price[p-1]*distance[p]
        price[p]=price[p-1]
    else:
        now+=price[p]*distance[p]
print(now)
